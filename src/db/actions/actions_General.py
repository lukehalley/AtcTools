"""
General Database Actions Module.

This module provides common database operations like executing queries
and running SQL scripts from files.
"""

from typing import Any, Dict, List

from mysql.connector import OperationalError
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()


def executeReadQuery(cursor: MySQLCursor, query: str) -> List[Dict[str, Any]]:
    """
    Execute a read query and return all results.

    Args:
        cursor: Database cursor to execute the query.
        query: SQL query string to execute.

    Returns:
        List of dictionaries containing query results.
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
    sql_commands = sql_content.split(';')

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