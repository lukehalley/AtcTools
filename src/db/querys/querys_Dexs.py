"""
DEX Query Module.

This module provides database query functions for retrieving DEX (Decentralized
Exchange) information from the database.
"""

from typing import Any, Dict, List

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery


def getAllDexsForNetwork(dbConnection: Any, networkDbId: int) -> List[Dict[str, Any]]:
    """
    Retrieve all DEXes for a specific network.

    Args:
        dbConnection: Active MySQL database connection.
        networkDbId: The database ID of the network to query.

    Returns:
        List of dictionaries containing DEX information including
        factory address, router address, and S3 paths for ABIs.
    """
    query = "" \
            f"SELECT * " \
            f"FROM dexs " \
            f"WHERE network_id={networkDbId}"

    cursor = getCursor(dbConnection=dbConnection)

    dexsDict = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return dexsDict

