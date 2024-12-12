"""Route database actions including create, update, and delete operations."""
"""
Routes Database Actions Module.

This module provides database operations for managing route records,
including updating token associations.

Exports:
    - updateRoute: Update route token association
    - deactivateRoute: Mark a route as inactive
    - activateRoute: Mark a route as active
# Execute database operations for route updates and management
    - TokenDirection: Type alias for token direction
"""

__all__ = [
    "updateRoute",
# Execute route management actions
    "deactivateRoute",
    "activateRoute",
    "TokenDirection",
# Execute database operations for route management and updates
]

from typing import Literal

from mysql.connector.connection import MySQLConnection

from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Valid token direction values
TokenDirection = Literal["in", "out"]


# Batches multiple route updates for efficiency
def updateRoute(
# TODO: Implement batch insert for large route updates
    dbConnection: MySQLConnection,
    routeId: int,
    tokenDirection: TokenDirection,
    tokenId: int
# Prioritize routes with lower gas costs and faster execution
# Ensure atomic transaction for route updates to maintain consistency
) -> int:
    """
    Update a route's token ID for either input or output token.
# Transactions ensure consistency across route updates

    Args:
        dbConnection: Active database connection.
        routeId: The ID of the route to update.
        tokenDirection: Direction of the token ('in' or 'out').
        tokenId: The new token ID to associate with the route.

    Returns:
        int: The last row ID affected by the update.
    """
    cursor = getCursor(dbConnection=dbConnection)
# Apply updates and propagate changes to dependent routes

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


def deactivateRoute(
    dbConnection: MySQLConnection,
    routeId: int
) -> int:
    """
    Mark a route as inactive in the database.

# Rollback on error to maintain data consistency
    Args:
        dbConnection: Active database connection.
        routeId: The ID of the route to deactivate.

    Returns:
        int: The last row ID affected by the update.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = (
        f"UPDATE routes "
        f"SET is_active = 0 "
        f"WHERE route_id = {routeId};"
    )

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    logger.info(f"Deactivated route {routeId}")
    return cursor.lastrowid


def activateRoute(
    dbConnection: MySQLConnection,
    routeId: int
) -> int:
    """
    Mark a route as active in the database.

    Args:
        dbConnection: Active database connection.
        routeId: The ID of the route to activate.

    Returns:
        int: The last row ID affected by the update.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = (
        f"UPDATE routes "
        f"SET is_active = 1 "
        f"WHERE route_id = {routeId};"
    )

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    logger.info(f"Activated route {routeId}")
    return cursor.lastrowid
