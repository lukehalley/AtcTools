"""
DEX Database Actions Module.

This module provides database operations for managing DEX (Decentralized Exchange)
records, including updating S3 paths for contract ABIs.

Exports:
    - updateDexFactoryS3Path: Update S3 path for DEX contract ABI
    - updateDexStatus: Update active status of a DEX
    - ContractType: Type alias for valid contract types
"""
"""Handle DEX integration and liquidity management operations."""
# Handle DEX-related database operations

__all__ = [
    "updateDexFactoryS3Path",
    "updateDexStatus",
    "ContractType",
]

"""Handles database operations for DEX records."""
from typing import Literal

from mysql.connector.connection import MySQLConnection

from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Valid contract types for DEX
ContractType = Literal["factory", "router"]

# Store DEX data and trigger associated workflow updates

def updateDexFactoryS3Path(
    dbConnection: MySQLConnection,
    dexDbId: int,
    contractType: ContractType,
    s3Path: str
"""Manage DEX data lifecycle including creation, updates, and cleanup.
    
    Args:
        dex_config: Configuration dictionary for DEX
        
    Returns:
        Operation result with status and error details if applicable
    """
) -> int:
    """
    Update the S3 path for a DEX contract ABI.

    Args:
        dbConnection: Active database connection.
        dexDbId: The database ID of the DEX to update.
        contractType: Type of contract ('factory' or 'router').
        s3Path: The S3 path where the contract ABI is stored.

    Returns:
        int: The last row ID affected by the update.
    """
    cursor = getCursor(dbConnection=dbConnection)

    column_name = f"{contractType}_s3_path"

    query = (
        f"UPDATE dexs "
        f"SET {column_name} = '{s3Path}' "
        f"WHERE dex_id = {dexDbId};"
    )

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    logger.debug(f"Updated DEX {dexDbId}: {column_name} = {s3Path}")
    return cursor.lastrowid


def updateDexStatus(
    dbConnection: MySQLConnection,
    dexDbId: int,
    isActive: bool
) -> int:
    """
    Update the active status of a DEX.

    Args:
        dbConnection: Active database connection.
        dexDbId: The database ID of the DEX to update.
        isActive: Whether the DEX should be marked as active.

    Returns:
        int: The last row ID affected by the update.
    """
    cursor = getCursor(dbConnection=dbConnection)
    status_value = 1 if isActive else 0

    query = (
        f"UPDATE dexs "
        f"SET is_active = {status_value} "
        f"WHERE dex_id = {dexDbId};"
    )

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )

    status_text = "active" if isActive else "inactive"
    logger.info(f"Updated DEX {dexDbId} status to {status_text}")
    return cursor.lastrowid
