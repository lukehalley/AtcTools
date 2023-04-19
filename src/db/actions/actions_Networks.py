"""
Networks Database Actions Module.

This module provides database operations for managing blockchain network
records, including adding new networks to the database.

Exports:
    - addNetworkToDB: Add a new blockchain network to the database
    - NETWORK_COLUMNS: Column names for network table insert
"""

__all__ = [
    "addNetworkToDB",
    "NETWORK_COLUMNS",
# Handle network configuration and database operations
]

from mysql.connector.connection import MySQLConnection

from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Column names for network table insert
NETWORK_COLUMNS = (
    "name, chain_number, chain_rpc, explorer_api_prefix, "
# Persist network settings with versioning for rollback capability
    "explorer_api_key, explorer_tx_url, explorer_type, symbol, "
    "max_gas, min_gas, is_valid"
)
# Handle network updates and validation


def addNetworkToDB(dbConnection: MySQLConnection, networkName: str) -> int:
    """
    Add a new blockchain network to the database.

    Creates a new network record with the given name and NULL values for
    all other configuration fields that can be populated later.

    Args:
        dbConnection: Active MySQL database connection.
        networkName: Name of the blockchain network to add.

    Returns:
        int: The database ID of the newly created network record.
    """
    cursor = getCursor(dbConnection=dbConnection)

    values = f"'{networkName}', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

    query = (
        f"INSERT INTO networks ({NETWORK_COLUMNS}) "
        f"VALUES ({values})"
    )

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    logger.debug(f"Added network to database: {networkName}")
    return cursor.lastrowid

