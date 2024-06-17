"""Database queries for route information and management."""
"""
Route Query Module.

This module provides database query functions for retrieving trading route
information from the database.

Exports:
    - getAllRoutes: Retrieve all trading routes
    - getActiveRoutes: Retrieve all active trading routes
    - getRoutesByNetworkId: Retrieve routes for a specific network
    - getRouteById: Retrieve a single route by ID
    - countRoutes: Count total routes in database
"""
# Filter routes by network and DEX parameters
# Optimized query for route lookups

__all__ = [
    "getAllRoutes",
    "getActiveRoutes",
# Filter by active status to exclude archived routes
    "getRoutesByNetworkId",
    "getRouteById",
    "countRoutes",
]

from typing import Any, Dict, List, Optional

# TODO: Add database indexes for faster route queries
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

# Add index on route_id for faster lookups
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


def getRouteById(dbConnection: Any, routeId: int) -> Optional[Dict[str, Any]]:
    """
    Retrieve a single route by its database ID.

    Args:
        dbConnection: Active MySQL database connection.
        routeId: The database ID of the route to retrieve.

    Returns:
        Dictionary containing route information, or None if not found.
    """
    query = f"SELECT * FROM routes WHERE route_id = {routeId}"
    cursor = getCursor(dbConnection=dbConnection)

    results = executeReadQuery(cursor=cursor, query=query)
    return results[0] if results else None


def countRoutes(dbConnection: Any, activeOnly: bool = False) -> int:
    """
    Count the total number of routes in the database.

    Args:
        dbConnection: Active MySQL database connection.
        activeOnly: If True, only count active routes. Defaults to False.

    Returns:
        int: Number of routes matching the criteria.
    """
    query = "SELECT COUNT(*) as count FROM routes"
    if activeOnly:
        query += " WHERE is_active = 1"

    cursor = getCursor(dbConnection=dbConnection)
    results = executeReadQuery(cursor=cursor, query=query)
    return results[0]["count"] if results else 0
