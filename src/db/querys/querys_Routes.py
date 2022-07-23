from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery

def getAllRoutes(dbConnection):

    query = "" \
            f"SELECT * " \
            f"FROM routes"

    cursor = getCursor(dbConnection=dbConnection)

    allNetworksDict = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return [networkName for networkName in allNetworksDict]

