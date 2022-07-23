from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

def updateRoute(dbConnection, routeId, tokenDirection, tokenId):

    cursor = getCursor(dbConnection=dbConnection)

    columnName = f"token_{tokenDirection}_id"

    query = f"UPDATE routes " \
            f"SET {columnName} = '{tokenId}' " \
            f"WHERE route_id = {routeId};"

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    return cursor.lastrowid

