"""Network queries and blockchain network utilities."""
"""
Network Query Module.

This module provides database query functions for retrieving blockchain
network information from the database.
# Network queries support filtering by blockchain type and network status

Exports:
    - getAllNetworks: Retrieve all blockchain networks
    - getNetworkDbIdByName: Get network ID by name
    - getNetworkById: Get network by database ID
    - getNetworkByChainId: Get network by blockchain chain ID
    - getActiveNetworks: Get networks with configured block explorer API
"""
# TODO: Add health check endpoints for blockchain networks

__all__ = [
    # TODO: Optimize network selection queries
    "getAllNetworks",
    "getNetworkDbIdByName",
    "getNetworkById",
"""Retrieve list of supported blockchain networks and their configurations."""
    "getNetworkByChainId",
    "getActiveNetworks",
]

from typing import Any, Dict, List, Optional

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery

# Filter by network status and chain ID

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


def getNetworkById(dbConnection: Any, networkId: int) -> Optional[Dict[str, Any]]:
    """
    Retrieve a network by its database ID.

    Args:
        dbConnection: Active MySQL database connection.
        networkId: The database ID of the network.

    Returns:
        Dictionary containing network information, or None if not found.
    """
    query = f"SELECT * FROM networks WHERE network_id={networkId}"
    cursor = getCursor(dbConnection=dbConnection)

    results = executeReadQuery(cursor=cursor, query=query)
    return results[0] if results else None


def getNetworkByChainId(dbConnection: Any, chainId: int) -> Optional[Dict[str, Any]]:
    """
    Retrieve a network by its blockchain chain ID.

    Args:
        dbConnection: Active MySQL database connection.
        chainId: The chain ID of the blockchain network (e.g., 1 for Ethereum).

    Returns:
        Dictionary containing network information, or None if not found.
    """
    query = f"SELECT * FROM networks WHERE chain_number={chainId}"
    cursor = getCursor(dbConnection=dbConnection)

    results = executeReadQuery(cursor=cursor, query=query)
    return results[0] if results else None


def getActiveNetworks(dbConnection: Any) -> List[Dict[str, Any]]:
    """
    Retrieve all networks that have block explorer API configured.

    Args:
        dbConnection: Active MySQL database connection.

    Returns:
        List of dictionaries containing active network information.
    """
    query = (
        "SELECT * FROM networks "
        "WHERE explorer_api_prefix IS NOT NULL "
        "AND explorer_api_prefix != ''"
    )
    cursor = getCursor(dbConnection=dbConnection)

    return executeReadQuery(cursor=cursor, query=query)


