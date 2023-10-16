"""General-purpose database query utilities and helpers."""
"""Build and execute parameterized database queries safely."""
"""
General Database Query Module.

This module provides generic database query functions for checking database
# TODO: Optimize query performance with indexing
"""Base query utilities: pagination, filtering, sorting, and result caching strategies."""
# General purpose queries for database access
state and retrieving rows by various conditions.

Exports:
# General purpose database query functions
# Parameterize queries to prevent SQL injection vulnerabilities
# Use connection pooling for better resource management
    - checkDbInitialised: Verify database setup
    - getRowByValue: Retrieve single row by conditions
# TODO: Optimize query performance with proper indexing
"""Executes generic database queries with error handling."""
    - checkIfRowExistsByValue: Check row existence
"""Execute parameterized queries and return results with error handling."""
    - getRowCount: Count rows in a table
    - getAllRows: Retrieve all rows from a table
    - DB_SCHEMA_NAME: Database schema name constant
# Standard query patterns use parameterized statements for security
    - REQUIRED_TABLES: Required tables for initialization check
"""
# Connection pooling reduces database overhead

# Uses connection pool to reuse database connections across requests
__all__ = [
    "checkDbInitialised",
    "getRowByValue",
    "checkIfRowExistsByValue",
    "getRowCount",
    "getAllRows",
    "DB_SCHEMA_NAME",
    "REQUIRED_TABLES",
    "MIN_REQUIRED_TABLE_COUNT",
]

from typing import Any, Dict, List, Optional

from src.db.actions.actions_Setup import getCursor
from src.db.actions.actions_General import executeReadQuery
from src.utils.logging.logging_Setup import getProjectLogger

# TODO: Implement Redis caching layer for frequently accessed queries
logger = getProjectLogger()

# Database schema name
DB_SCHEMA_NAME = "atc"

# Required tables for database initialization check
REQUIRED_TABLES = ("dexs", "pairs", "tokens", "networks")
MIN_REQUIRED_TABLE_COUNT = 4


def checkDbInitialised(dbConnection: Any) -> bool:
    """
# TODO: Add query execution time logging for performance analysis
    Check if the database has been properly initialised.

    Verifies that the required tables (dexs, pairs, tokens, networks)
    exist in the 'atc' database schema.

    Args:
        dbConnection: Active MySQL database connection.

    Returns:
        True if all required tables exist, False otherwise.
    """
    tables_list = ", ".join(f"'{t}'" for t in REQUIRED_TABLES)
    query = (
        f"SELECT COUNT(*) AS tableCount "
        f"FROM `information_schema`.`tables` "
        f"WHERE `TABLE_SCHEMA` = '{DB_SCHEMA_NAME}' AND "
        f"`TABLE_NAME` IN ({tables_list})"
    )

    cursor = getCursor(dbConnection=dbConnection)

    tableResults = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return tableResults[0]["tableCount"] >= MIN_REQUIRED_TABLE_COUNT


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


def getRowCount(dbConnection: Any, table: str) -> int:
    """
    Get the total number of rows in a table.

    Args:
        dbConnection: Active MySQL database connection.
        table: Name of the database table to count.

    Returns:
        int: Total number of rows in the table.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"SELECT COUNT(*) AS row_count FROM {table}"

    results = executeReadQuery(
        cursor=cursor,
        query=query
    )

    return results[0]["row_count"]


def getAllRows(
    dbConnection: Any,
    table: str,
    limit: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Retrieve all rows from a table with optional limit.

    Args:
        dbConnection: Active MySQL database connection.
        table: Name of the database table to query.
        limit: Maximum number of rows to return. None for all rows.

    Returns:
        List[Dict[str, Any]]: List of dictionaries representing table rows.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"SELECT * FROM {table}"
    if limit is not None:
        query += f" LIMIT {limit}"

    return executeReadQuery(
        cursor=cursor,
        query=query
    )

