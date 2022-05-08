from src.db.actions.actions_Setup import initDBConnection
from src.db.querys.querys_Dexs import getAllDexsForNetwork
from src.db.querys.querys_Networks import getAllNetworks

import aiohttp
import asyncio
import time

from src.utils.web.web_RateLimiter import RateLimiter

start_time = time.time()


async def getAbi(clientSession, rateLimiter, networkName, dexName, contractType, apiURL):
    async with rateLimiter.throttle():
        response = await clientSession.get(apiURL)

    responseJSON = await response.json()

    if int(responseJSON["status"]) == 1:
        print(f"{networkName.title()} | {dexName.title()} | {contractType.title()} ✅")
        result = responseJSON["result"]
    else:
        print(f"{networkName.title()} | {dexName.title()} | {contractType.title()} | {responseJSON['result']} ⛔️")
        result = None

    response.release()
    return result


async def main():
    dbConnection = initDBConnection()

    networks = getAllNetworks(dbConnection=dbConnection)

    networksWithAPIKeys = [network for network in networks if network["explorer_api_key"]]

    async with RateLimiter(rate_limit=3, concurrency_limit=1000) as rate_limiter:

        async with aiohttp.ClientSession() as session:

            tasks = []
            for network in networksWithAPIKeys:

                dexs = getAllDexsForNetwork(
                    dbConnection=dbConnection,
                    networkDbId=network["network_id"]
                )

                dexsWithAddresses = [dex for dex in dexs if dex["factory"] and dex["router"]]

                for dex in dexsWithAddresses:

                    contractAbisToGet = ["factory", "router"]

                    for contract in contractAbisToGet:
                        apiEndpoint = network["explorer_api_prefix"]
                        apiToken = network["explorer_api_key"]
                        contractAddress = dex[contract]
                        normalisedContractAddress = ''.join(e for e in contractAddress if e.isalnum())

                        apiUrl = f"{apiEndpoint}/api?module=contract&action=getabi&address={normalisedContractAddress}&apikey={apiToken}"
                        tasks.append(
                            asyncio.ensure_future(getAbi(clientSession=session,
                                                         rateLimiter=rate_limiter,
                                                         networkName=network["name"],
                                                         dexName=dex["name"],
                                                         apiURL=apiUrl,
                                                         contractType=contract
                                                         )
                                                  ))

            allAbis = await asyncio.gather(*tasks)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
