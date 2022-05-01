import asyncio

from src.blockExplorer.blockExplorer_ABI import getAbiForNetworks
from src.db.actions.actions_Setup import initDBConnection
from src.db.querys.querys_Networks import getAllNetworks

def collectAbis():

    dbConnection = initDBConnection()

    networks = getAllNetworks(dbConnection=dbConnection)

    networksWithAPIKeys = [network for network in networks if network["explorer_api_key"]]

    asyncio.run(
        getAbiForNetworks(
            dbConnection=dbConnection,
            networks=networksWithAPIKeys
        )
    )