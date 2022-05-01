import asyncio
import time

import requests
from ratelimit import limits

from src.db.querys.querys_Dexs import getAllDexsForNetwork


@limits(calls=5, period=1)
def getAbiForNetwork(apiEndpoint, apiToken, contractAddress):

    normalisedContractAddress = ''.join(e for e in contractAddress if e.isalnum())

    apiUrl = f"{apiEndpoint}/api?module=contract&action=getabi&address={normalisedContractAddress}&apikey={apiToken}"

    try:

        result = requests.get(url=apiUrl).json()

        if "result" in result:
            result = result["result"]

    except ValueError:
        result = None

    return result

def getAbisForNetworkDexs(dbConnection, apiEndpoint, apiToken, networkDbId):

    dexs = getAllDexsForNetwork(
        dbConnection=dbConnection,
        networkDbId=networkDbId
    )

    dexsWithAddresses = [dex for dex in dexs if dex["factory"] and dex["router"]]

    for dex in dexsWithAddresses:

        contractAbisToGet = ["factory", "router"]

        for contract in contractAbisToGet:

            contractAbi = getAbiForNetwork(
                apiEndpoint=apiEndpoint,
                apiToken=apiToken,
                contractAddress=dex[contract]
            )

            dex[f"{contract}ABI"] = contractAbi

            print(contractAbi)

    return dexsWithAddresses

async def getAbiForNetworks(dbConnection, networks):

    tasks = [getAbisForNetworkDexs(
        dbConnection=dbConnection,
        apiEndpoint=network["explorer_api_prefix"],
        apiToken=network["explorer_api_key"],
        networkDbId=network["network_id"]
    ) for network in networks]

    gatheredNetworkAbis = await asyncio.gather(*tasks)

    x = 1