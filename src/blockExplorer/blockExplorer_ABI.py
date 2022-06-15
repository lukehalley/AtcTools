import asyncio
import json
import os
import urllib.request
import urllib.request

import aiohttp

from src.aws.aws_s3 import writeJSONToS3, getCurrentStoredABIs
from src.db.actions.actions_Dexs import updateDexFactoryS3Path
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

async def getAbi(clientSession, dbConnection, rateLimiter, networkName, dexDbId, dexName, contractType, apiURL):
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

            s3Path = f"{networkName}/{dexName}/{contractType}.json"

            fileUploaded = writeJSONToS3(
                jsonData=jsonObject,
                s3Path=s3Path
            )

            if fileUploaded:
                updateDexFactoryS3Path(
                    dbConnection=dbConnection,
                    dexDbId=dexDbId,
                    contractType=contractType,
                    s3Path=s3Path
                )

        else:
            logger.info(f"{networkName.title()} | {dexName.title()} | {contractType.title()} | Bad ABI ⚠️️")
            result = None

    else:

        errorMessage = responseJSON['result']

        if not errorMessage:
            errorMessage = responseJSON["message"]

            if not errorMessage:
                errorMessage = "Unknown error!"

        logger.info(f"{networkName.title()} | {dexName.title()} | {contractType.title()} | {errorMessage} ⛔️\n")
        result = None

    response.release()
    return result

async def collectAbis():

    dbConnection = initDBConnection()

    networks = getAllNetworks(dbConnection=dbConnection)

    validNetworks = [network for network in networks if (network["explorer_type"] == "scan" or network["explorer_type"] == "blockscout") and network["explorer_api_prefix"]]

    s3Bucket = os.getenv("S3_BUCKET")

    async with RateLimiter(rate_limit=3, concurrency_limit=1000) as rate_limiter:

        async with aiohttp.ClientSession() as session:

            tasks = []
            for network in validNetworks:

                networkName = network["name"]

                dexs = getAllDexsForNetwork(
                    dbConnection=dbConnection,
                    networkDbId=network["network_id"]
                )

                dexsWithAddresses = [dex for dex in dexs if dex["factory"] and dex["router"]]

                uploadedAbis = getCurrentStoredABIs(
                    networkName=networkName
                )

                for dex in dexsWithAddresses:

                    dexName = dex["name"]
                    dexDbId = dex["dex_id"]

                    contractAbisToGet = ["factory", "router"]

                    for contract in contractAbisToGet:

                        predictedS3Key = f"{networkName}/{dexName}/{contract}.json"

                        if not predictedS3Key in uploadedAbis:

                            apiEndpoint = network["explorer_api_prefix"]
                            apiToken = network["explorer_api_key"]
                            contractAddress = dex[contract]
                            normalisedContractAddress = ''.join(e for e in contractAddress if e.isalnum())

                            apiUrl = f"{apiEndpoint}/api?module=contract&action=getabi&address={normalisedContractAddress}"

                            if apiToken:
                                apiUrl = f"{apiUrl}&apikey={apiToken}"

                            tasks.append(
                                asyncio.ensure_future(getAbi(clientSession=session,
                                                             dbConnection=dbConnection,
                                                             rateLimiter=rate_limiter,
                                                             networkName=networkName,
                                                             dexName=dexName,
                                                             dexDbId=dexDbId,
                                                             apiURL=apiUrl,
                                                             contractType=contract
                                                             )
                                                      ))

                        else:

                            logger.info(f"File {predictedS3Key} already exists in {s3Bucket}\n")

            collectedAbis = await asyncio.gather(*tasks)

            logger.info("All ABIs Collected ✅")