"""
DEX Database Actions Module.

This module provides database operations for managing DEX (Decentralized Exchange)
records, including updating S3 paths for contract ABIs.
"""

from typing import Literal

from mysql.connector.connection import MySQLConnection

from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Valid contract types for DEX
ContractType = Literal["factory", "router"]


def updateDexFactoryS3Path(
    dbConnection: MySQLConnection,
    dexDbId: int,
    contractType: ContractType,
    s3Path: str
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

