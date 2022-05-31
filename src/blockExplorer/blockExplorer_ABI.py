import asyncio
import json
import urllib.request
import urllib.request

import aiohttp

from src.aws.aws_s3 import writeJSONToS3
from src.db.actions.actions_Setup import initDBConnection
from src.db.querys.querys_Dexs import getAllDexsForNetwork
from src.db.querys.querys_Networks import getAllNetworks
from src.utils.logging.logging_Setup import getProjectLogger
from src.utils.web.web_RateLimiter import RateLimiter

logger = getProjectLogger()

def getUniswapGenericAbis():
    uniswapFactoryURL = "https://unpkg.com/@uniswap/v2-core@1.0.0/build/IUniswapV2Factory.json"
    uniswapRouterURL = "https://unpkg.com/@uniswap/v2-periphery@1.0.0-beta.0/build/IUniswapV2Router01.json"

    with urllib.request.urlopen(uniswapFactoryURL) as url:
        uniswapFactory = json.load(url)["abi"]

    with urllib.request.urlopen(uniswapRouterURL) as url:
        uniswapRouter = json.load(url)["abi"]

    return uniswapFactory, uniswapRouter

async def getAbi(clientSession, rateLimiter, networkName, dexName, contractType, apiURL):
    async with rateLimiter.throttle():
        response = await clientSession.get(apiURL)

    responseJSON = await response.json()

    if int(responseJSON["status"]) == 1:

        jsonObject = json.loads(responseJSON["result"])

        validAbi = "stateMutability" in jsonObject[-1]

        if validAbi:

            logger.info(f"{networkName.title()} | {dexName.title()} | {contractType.title()} ✅")

            result = {
                "networkName": networkName,
                "dexName": dexName,
                "contractType": contractType,
                "contractAbi": jsonObject
            }

            s3Path = f"{networkName}/{dexName}/{contractType}"

            writeJSONToS3(
                jsonData=jsonObject,
                s3Path=s3Path
            )

        else:
            logger.info(f"{networkName.title()} | {dexName.title()} | {contractType.title()} | Bad ABI ⚠️️")
            result = None

    else:
        logger.info(f"{networkName.title()} | {dexName.title()} | {contractType.title()} | {responseJSON['result']} ⛔️\n")
        result = None

    response.release()
    return result

async def collectAbis():
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

            await asyncio.gather(*tasks)

            logger.info("All ABIs Collected ✅")