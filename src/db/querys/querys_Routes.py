"""
Route Query Module.

This module provides database query functions for retrieving trading route
information from the database.
"""

from typing import Any, Dict, List

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery


def getAllRoutes(dbConnection: Any) -> List[Dict[str, Any]]:
    """
    Retrieve all trading routes from the database.

    Args:
        dbConnection: Active MySQL database connection.

    Returns:
        List of dictionaries containing route information including
        network ID, DEX ID, token addresses, and transaction details.
    """
    query = "" \
            f"SELECT * " \
            f"FROM routes"

    cursor = getCursor(dbConnection=dbConnection)

    allRoutesDict = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return [route for route in allRoutesDict]


def getActiveRoutes(dbConnection: Any) -> List[Dict[str, Any]]:
    """
    Retrieve all active trading routes from the database.

    Args:
        dbConnection: Active MySQL database connection.

    Returns:
        List of dictionaries containing active route information.
    """
    query = (
        "SELECT * FROM routes "
        "WHERE is_active = 1"
    )

    cursor = getCursor(dbConnection=dbConnection)
    return executeReadQuery(cursor=cursor, query=query)


def getRoutesByNetworkId(dbConnection: Any, networkId: int) -> List[Dict[str, Any]]:
    """
    Retrieve all routes for a specific network.

    Args:
        dbConnection: Active MySQL database connection.
        networkId: The database ID of the network.

    Returns:
        List of dictionaries containing route information for the network.
    """
    query = f"SELECT * FROM routes WHERE network_id = {networkId}"

    cursor = getCursor(dbConnection=dbConnection)
    return executeReadQuery(cursor=cursor, query=query)
