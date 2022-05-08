import asyncio
import time

import requests
from ratelimit import limits

from src.db.querys.querys_Dexs import getAllDexsForNetwork


@limits(calls=5, period=1)
def getAbi(apiEndpoint, apiToken, contractAddress):

    normalisedContractAddress = ''.join(e for e in contractAddress if e.isalnum())

    apiUrl = f"{apiEndpoint}/api?module=contract&action=getabi&address={normalisedContractAddress}&apikey={apiToken}"

    try:

        result = requests.get(url=apiUrl).json()

        if "result" in result:
            result = result["result"]

    except ValueError:
        result = None

    return result

async def getAbisForNetworkDexs(dbConnection, networkName, networkDbId, apiEndpoint, apiToken):

    print(networkName.title())

    dexs = getAllDexsForNetwork(
        dbConnection=dbConnection,
        networkDbId=networkDbId
    )

    dexsWithAddresses = [dex for dex in dexs if dex["factory"] and dex["router"]]

    for dex in dexsWithAddresses:

        contractAbisToGet = ["factory", "router"]

        for contract in contractAbisToGet:

            contractAbi = getAbi(
                apiEndpoint=apiEndpoint,
                apiToken=apiToken,
                contractAddress=dex[contract]
            )

            dex[f"{contract}ABI"] = contractAbi

        print(f'  - {dex["name"]} ✅')

    return dexsWithAddresses