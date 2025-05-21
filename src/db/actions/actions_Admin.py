"""
Database Administration Module.

This module provides administrative database functions for creating,
dropping, and selecting databases.
"""

from typing import Any

from src.db.actions.actions_General import executeWriteQuery
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Default database name for ATC application
DEFAULT_DATABASE_NAME = "atc"


def createDatabase(dbConnection: Any, databaseName: str = DEFAULT_DATABASE_NAME) -> None:
    """
    Create a new database if it does not already exist.

    Args:
        dbConnection: Active MySQL database connection.
        databaseName: Name of the database to create.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"CREATE DATABASE IF NOT EXISTS {databaseName}"

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )


def dropDatabase(dbConnection: Any, databaseName: str = DEFAULT_DATABASE_NAME) -> None:
    """
    Drop an existing database if it exists.

    Args:
        dbConnection: Active MySQL database connection.
        databaseName: Name of the database to drop.

    Warning:
        This operation is destructive and cannot be undone.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"DROP DATABASE IF EXISTS {databaseName}"

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )


def useDatabase(dbConnection: Any, databaseName: str = DEFAULT_DATABASE_NAME) -> None:
    """
    Switch to the specified database for subsequent queries.

    Args:
        dbConnection: Active MySQL database connection.
        databaseName: Name of the database to use.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"USE {databaseName}"

    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )


def checkDatabaseExists(dbConnection: Any, databaseName: str = DEFAULT_DATABASE_NAME) -> bool:
    """
    Check if a database exists.

    Args:
        dbConnection: Active MySQL database connection.
        databaseName: Name of the database to check.

    Returns:
        bool: True if the database exists, False otherwise.
    """
    cursor = getCursor(dbConnection=dbConnection)

    query = f"SHOW DATABASES LIKE '{databaseName}'"
    cursor.execute(query)
    result = cursor.fetchall()

    exists = len(result) > 0
    logger.debug(f"Database '{databaseName}' exists: {exists}")
    return exists