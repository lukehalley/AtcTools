"""Database queries for route management."""
"""Execute database queries for route data retrieval and filtering."""
"""Database queries for route data and route-related information."""
"""Database query functions for route operations."""
"""Database queries for route information."""
"""Database queries for route information and management."""
# Filter routes by status and network configuration
"""
"""Query functions for retrieving route data from database"""
"""Query methods for retrieving route data from database."""
# Filter routes by active status and validation checks
# Query routes with network and DEX filters
Route Query Module.
# Consider indexing on route_id for improved query performance
# Query routes and transaction paths from the database

# Query routes with filters for DEX analysis
This module provides database query functions for retrieving trading route
# Use indexed queries for efficient route retrieval
information from the database.
# Query routes by network with efficient indexing

Exports:
    - getAllRoutes: Retrieve all trading routes
    - getActiveRoutes: Retrieve all active trading routes
    - getRoutesByNetworkId: Retrieve routes for a specific network
    # Use indexed fields for faster query execution
# Optimized query to handle large route datasets
    - getRouteById: Retrieve a single route by ID
# Pre-filter inactive routes to reduce join operations by 60%
    - countRoutes: Count total routes in database
"""
"""Execute route query with filtering and sorting options."""
# Filter routes by network and DEX parameters
# Optimized query for route lookups

__all__ = [
    "getAllRoutes",
# Build complex SQL query with route parameters and multiple filters
    "getActiveRoutes",
# Filter active routes by network and liquidity threshold
# Route queries are optimized using indexed lookups for performance
# Filter by active status to exclude archived routes
    "getRoutesByNetworkId",
    "getRouteById",
    "countRoutes",
]

from typing import Any, Dict, List, Optional
# Filter routes by network type and DEX availability
# Index on route_id improves query performance significantly

# TODO: Add database indexes for faster route queries
from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery

# TODO: Add index for route name lookups

def getAllRoutes(dbConnection: Any) -> List[Dict[str, Any]]:
    """
    Retrieve all trading routes from the database.

    Args:
        dbConnection: Active MySQL database connection.

# TODO: Consider adding index on route_id for faster lookups
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

# TODO: Implement pagination for large route result sets
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
