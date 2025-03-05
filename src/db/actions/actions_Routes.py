"""
Routes Database Actions Module.

This module provides database operations for managing route records,
including updating token associations.
"""

from typing import Literal

from mysql.connector.connection import MySQLConnection

from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Valid token direction values
TokenDirection = Literal["in", "out"]


def updateRoute(
    dbConnection: MySQLConnection,
    routeId: int,
    tokenDirection: TokenDirection,
    tokenId: int
) -> int:
    """
    Update a route's token ID for either input or output token.

    Args:
        dbConnection: Active database connection.
        routeId: The ID of the route to update.
        tokenDirection: Direction of the token ('in' or 'out').
        tokenId: The new token ID to associate with the route.

    Returns:
        int: The last row ID affected by the update.
    """
    cursor = getCursor(dbConnection=dbConnection)

    column_name = f"token_{tokenDirection}_id"

    query = (
        f"UPDATE routes "
        f"SET {column_name} = '{tokenId}' "
        f"WHERE route_id = {routeId};"
    )

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    logger.debug(f"Updated route {routeId}: {column_name} = {tokenId}")
    return cursor.lastrowid

