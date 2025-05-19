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

