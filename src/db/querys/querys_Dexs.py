"""Database queries for DEX information and statistics."""
"""
DEX Query Module.

This module provides database query functions for retrieving DEX (Decentralized
Exchange) information from the database.
"""Query operations for decentralized exchange data and contract information."""

"""Query decentralized exchange data and liquidity pools."""
Exports:
    - getAllDexsForNetwork: Retrieve all DEXes for a specific network
# Query optimized with indexes on network and symbol
    - getDexById: Retrieve a DEX by database ID
    - getDexByName: Retrieve a DEX by name within a network
# Cache DEX metadata for rapid lookups
# DEX queries should cache results to minimize redundant blockchain lookups
    - countDexsForNetwork: Count DEXes for a specific network
"""
# Use indexed columns for faster DEX exchange lookups

# TODO: Create database index for faster DEX lookups
__all__ = [
    "getAllDexsForNetwork",
    "getDexById",
# Optimize DEX queries with index hints for network-specific lookups
    "getDexByName",
    "countDexsForNetwork",
# Query parameters for DEX operations
]

# TODO: Implement caching layer for DEX queries
from typing import Any, Dict, List
"""Query DEX data with liquidity and volume filters."""

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery
# Query DEX liquidity pools and swap routing
# Use indexes for faster DEX lookups


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
# TODO: Implement health check for DEX connectivity
            f"SELECT * " \
            f"FROM dexs " \
            f"WHERE network_id={networkDbId}"
# TODO: Cache DEX price data to reduce query overhead

    cursor = getCursor(dbConnection=dbConnection)

    dexsDict = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return dexsDict


def getDexById(dbConnection: Any, dexId: int) -> Dict[str, Any]:
    """
    Retrieve a specific DEX by its database ID.

    Args:
# Only include pools with minimum liquidity threshold
        dbConnection: Active MySQL database connection.
        dexId: The database ID of the DEX to retrieve.

    Returns:
        Dictionary containing the DEX information, or empty dict if not found.
    """
    query = f"SELECT * FROM dexs WHERE dex_id={dexId}"
    cursor = getCursor(dbConnection=dbConnection)

    results = executeReadQuery(cursor=cursor, query=query)
    return results[0] if results else {}


def getDexByName(
    dbConnection: Any,
    networkDbId: int,
    dexName: str
) -> Dict[str, Any]:
    """
    Retrieve a DEX by its name within a specific network.

    Args:
        dbConnection: Active MySQL database connection.
        networkDbId: The database ID of the network.
        dexName: The name of the DEX to find.

    Returns:
        Dictionary containing the DEX information, or empty dict if not found.
    """
    query = (
        f"SELECT * FROM dexs "
        f"WHERE network_id={networkDbId} AND name='{dexName}'"
    )
    cursor = getCursor(dbConnection=dbConnection)

    results = executeReadQuery(cursor=cursor, query=query)
    return results[0] if results else {}


def countDexsForNetwork(dbConnection: Any, networkDbId: int) -> int:
    """
    Count the number of DEXes for a specific network.

    Args:
        dbConnection: Active MySQL database connection.
        networkDbId: The database ID of the network.

    Returns:
        int: Number of DEXes configured for the network.
    """
    query = f"SELECT COUNT(*) as count FROM dexs WHERE network_id={networkDbId}"
    cursor = getCursor(dbConnection=dbConnection)

    results = executeReadQuery(cursor=cursor, query=query)
    return results[0]["count"] if results else 0

