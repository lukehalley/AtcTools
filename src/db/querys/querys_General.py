"""
General Database Query Module.

This module provides generic database query functions for checking database
state and retrieving rows by various conditions.
"""

from typing import Any, Dict, List, Optional

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()


def checkDbInitialised(dbConnection: Any) -> bool:
    """
    Check if the database has been properly initialised.

    Verifies that the required tables (dexs, pairs, tokens, networks)
    exist in the 'atc' database schema.

    Args:
        dbConnection: Active MySQL database connection.

    Returns:
        True if all required tables exist, False otherwise.
    """
    query = "" \
            "SELECT COUNT(*) AS tableCount " \
            "FROM `information_schema`.`tables` " \
            "WHERE `TABLE_SCHEMA` = 'atc' AND " \
            "`TABLE_NAME` IN ('dexs', 'pairs', 'tokens', 'networks')"

    cursor = getCursor(dbConnection=dbConnection)

    tableResults = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return tableResults[0]["tableCount"] >= 4


def getRowByValue(
    dbConnection: Any,
    table: str,
    conditions: List[Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """
    Retrieve a single row from a table matching the given conditions.

    Args:
        dbConnection: Active MySQL database connection.
        table: Name of the database table to query.
        conditions: List of condition dictionaries, each containing
                   a single key-value pair for the WHERE clause.

    Returns:
        Dictionary containing the row data if found, None otherwise.
    """
    cursor = getCursor(dbConnection=dbConnection)

    amountOfConditions = len(conditions)

    columnName = list(conditions[0].keys())[0]
    rowValue = conditions[0][columnName]

    query = f"SELECT * FROM " \
            f"{table} WHERE " \
            f"{columnName}='{rowValue}'"

    if amountOfConditions > 1:

        del conditions[0]

        for condition in conditions:
            columnName = list(condition.keys())[0]
            rowValue = condition[columnName]

            query = \
                query + \
                " AND WHERE " \
                f"{columnName}='{rowValue}'"

    results = executeReadQuery(
        cursor=cursor,
        query=query
    )

    if results:
        return results[0]
    else:
        return None

def checkIfRowExistsByValue(
    dbConnection: Any,
    table: str,
    column: str,
    value: Any
) -> bool:
    """
    Check if a row exists in a table with the specified column value.

    Args:
        dbConnection: Active MySQL database connection.
        table: Name of the database table to query.
        column: Name of the column to check.
        value: Value to search for in the specified column.

    Returns:
        True if at least one matching row exists, False otherwise.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"SELECT COUNT(*) count FROM " \
            f"{table} WHERE " \
            f"{column}='{value}'"

    results = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return bool(results[0]["count"])

