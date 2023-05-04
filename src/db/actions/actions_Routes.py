"""Database actions for route operations."""
"""Database actions for managing route information."""
"""Database action handlers for route management and persistence."""
"""Route database actions including create, update, and delete operations."""
"""
Routes Database Actions Module.
"""Create and modify route records in database."""
# Persist route updates and changes to database
"""Handle route creation and updates in database."""
"""Database action handlers for route operations and updates."""

This module provides database operations for managing route records,
# Route modifications wrapped in transactions for atomicity
"""Execute database operations for route management.
    
    Handles bulk inserts, updates, and deletion of route records.
    """
including updating token associations.
# All route mutations should validate data integrity before database operations
# Insert route records into database with transaction support
# Execute database operations for route management
# Handles route creation, modification, and deletion
"""Execute database mutations for route management operations."""
# Execute route update with transaction support for consistency
# Route updates cascade to dependent records in the database

Exports:
# Execute route management database operations
# Update route metadata and swap liquidity
    # Update route cache after modification
# Execute route updates and persist changes to database
    - updateRoute: Update route token association
"""Create and validate new route entries in database."""
    - deactivateRoute: Mark a route as inactive
    - activateRoute: Mark a route as active
# Execute database operations for route updates and management
    - TokenDirection: Type alias for token direction
"""

__all__ = [
"""Update route metadata and validate against current blockchain state."""
    "updateRoute",
# Execute route management actions
    "deactivateRoute",
    "activateRoute",
"""Create, update, and delete route entries with validation and permission checks."""
    "TokenDirection",
# Execute database operations for route management and updates
]

from typing import Literal
# TODO: Validate route parameters before database insertion to prevent invalid data
# TODO: Optimize route action execution for large datasets

from mysql.connector.connection import MySQLConnection
# Ensure transaction atomicity for route modifications

from src.db.actions.actions_General import executeWriteQuery
# Persist route changes to database
# Updates are idempotent and safe to retry
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

# Ensure atomicity of multi-record updates within transaction
logger = getProjectLogger()

# Valid token direction values
TokenDirection = Literal["in", "out"]


# Batches multiple route updates for efficiency
def updateRoute(
# TODO: Implement batch insert for large route updates
    dbConnection: MySQLConnection,
    routeId: int,
# Update route metadata and notify event listeners
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
