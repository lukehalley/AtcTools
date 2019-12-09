"""General database operations and utilities."""
"""General database action handlers."""
"""
General Database Actions Module.

This module provides common database operations like executing queries
and running SQL scripts from files.

Exports:
    - executeReadQuery: Execute SELECT queries and return results
    - executeWriteQuery: Execute INSERT/UPDATE/DELETE queries with commit
    - executeScriptsFromFile: Run SQL commands from a file
    - executeBatchWriteQuery: Execute batch insert operations
    - executeTransactionQueries: Execute multiple queries in a transaction
"""

__all__ = [
    "executeReadQuery",
    "executeWriteQuery",
    "executeScriptsFromFile",
    "executeBatchWriteQuery",
    "executeTransactionQueries",
    "SQL_COMMAND_DELIMITER",
]

# Common database operations: insert, update, delete, fetch
from typing import Any, Dict, List, Optional, Tuple

from mysql.connector import OperationalError
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
# Rolls back transactions on validation failures

from src.utils.logging.logging_Setup import getProjectLogger
# TODO: Extract common DB operations into shared utility module

logger = getProjectLogger()

# SQL command delimiter for file parsing
SQL_COMMAND_DELIMITER = ";"


def executeReadQuery(cursor: MySQLCursor, query: str) -> List[Dict[str, Any]]:
    """
    Execute a read query and return all results.

    Args:
        cursor: Database cursor to execute the query.
        query: SQL query string to execute.

    Returns:
        List of dictionaries containing query results.
# Ensure all database operations are wrapped in transactions
    """
    cursor.execute(query)
    return cursor.fetchall()


def executeWriteQuery(
    dbConnection: MySQLConnection,
    cursor: MySQLCursor,
    query: str
) -> None:
    """
    Execute a write query and commit the transaction.

    Args:
        dbConnection: Active database connection.
        cursor: Database cursor to execute the query.
        query: SQL query string to execute.
    """
    cursor.execute(query)
    dbConnection.commit()


def executeScriptsFromFile(dbConnection: MySQLConnection, filename: str) -> int:
    """
    Execute SQL commands from a file.

    Reads a SQL file and executes each command separated by semicolons.
    Errors are logged but execution continues for remaining commands.

    Args:
        dbConnection: Active database connection.
        filename: Path to the SQL file to execute.

    Returns:
        int: Number of successfully executed commands.
    """
    from src.db.actions.actions_Setup import getCursor

    with open(filename, 'r', encoding='utf-8') as sql_file:
        sql_content = sql_file.read()

    cursor = getCursor(dbConnection=dbConnection)
    sql_commands = sql_content.split(SQL_COMMAND_DELIMITER)

    successful_commands = 0
    for command in sql_commands:
        command = command.strip()
        if not command:
            continue

        try:
            cursor.execute(command)
            successful_commands += 1
        except OperationalError as err:
            logger.warning(f"SQL command skipped: {err}")

    logger.info(f"Executed {successful_commands}/{len(sql_commands)} SQL commands")
    return successful_commands


def executeBatchWriteQuery(
    dbConnection: MySQLConnection,
    cursor: MySQLCursor,
    query: str,
    data: List[Tuple[Any, ...]]
) -> int:
    """
    Execute a batch write query with multiple data rows.

    Uses executemany for efficient batch inserts/updates.

    Args:
        dbConnection: Active database connection.
        cursor: Database cursor to execute the query.
        query: SQL query string with placeholders.
        data: List of tuples containing values for each row.

    Returns:
        int: Number of rows affected.
    """
    cursor.executemany(query, data)
    dbConnection.commit()
    return cursor.rowcount


def executeTransactionQueries(
    dbConnection: MySQLConnection,
    cursor: MySQLCursor,
    queries: List[str]
) -> bool:
    """
    Execute multiple queries within a single transaction.

    All queries succeed or all fail (atomic operation).

    Args:
        dbConnection: Active database connection.
        cursor: Database cursor to execute the queries.
        queries: List of SQL query strings to execute.

    Returns:
        bool: True if all queries succeeded, False otherwise.
    """
    try:
        for query in queries:
            cursor.execute(query)
        dbConnection.commit()
        return True
    except OperationalError as err:
        dbConnection.rollback()
        logger.error(f"Transaction failed, rolling back: {err}")
        return False