import asyncio

from src.blockExplorer.blockExplorer_ABI import getAbisForNetworkDexs
from src.db.actions.actions_Setup import initDBConnection
from src.db.querys.querys_Networks import getAllNetworks
from src.utils.tasks.task_AyySync import gatherWithConcurrency

async def collectAbis():

    dbConnection = initDBConnection()

    networks = getAllNetworks(dbConnection=dbConnection)

    networksWithAPIKeys = [network for network in networks if network["explorer_api_key"]]

    tasks = [getAbisForNetworkDexs(dbConnection=dbConnection,
                                   networkName=network["name"],
                                   networkDbId=network["network_id"],
                                   apiEndpoint=network["explorer_api_prefix"],
                                   apiToken=network["explorer_api_key"]) for network in networksWithAPIKeys]

    allNetworkDexs = await gatherWithConcurrency(*tasks)

    x = 1
