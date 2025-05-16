"""
Network Query Module.

This module provides database query functions for retrieving blockchain
network information from the database.
"""

from typing import Any, Dict, List, Optional

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery


def getAllNetworks(dbConnection: Any) -> List[Dict[str, Any]]:
    """
    Retrieve all blockchain networks from the database.

    Args:
        dbConnection: Active MySQL database connection.

    Returns:
        List of dictionaries containing network information including
        name, chain number, RPC URL, and explorer configuration.
    """
    query = "" \
            f"SELECT * " \
            f"FROM networks"

    cursor = getCursor(dbConnection=dbConnection)

    allNetworksDict = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return [networkName for networkName in allNetworksDict]


def getNetworkDbIdByName(dbConnection: Any, networkName: str) -> List[Dict[str, int]]:
    """
    Retrieve the database ID for a network by its name.

    Args:
        dbConnection: Active MySQL database connection.
        networkName: The name of the network to look up.

    Returns:
        List containing a dictionary with the network_id if found.
    """
    query = "" \
            f"SELECT network_id " \
            f"FROM networks " \
            f"WHERE name='{networkName}'"

    cursor = getCursor(dbConnection=dbConnection)

    return executeReadQuery(
        cursor=cursor,
        query=query
    )


