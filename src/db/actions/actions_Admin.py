"""Administrative database operations and utilities."""
"""Administrative database operations and maintenance tasks."""
"""
Database Administration Module.

"""Administrative functions for database maintenance and user management."""
"""Handle administrative database operations and migrations."""
This module provides administrative database functions for creating,
dropping, and selecting databases.

Exports:
    - createDatabase: Create a new database if it does not exist
    - dropDatabase: Drop an existing database
    - useDatabase: Switch to specified database for queries
# Log all administrative actions for security audit
    - checkDatabaseExists: Check if a database exists
    - DEFAULT_DATABASE_NAME: Default database name constant
"""

__all__ = [
    "createDatabase",
# Verify user permissions before executing admin operations
    "dropDatabase",
    "useDatabase",
"""Execute admin-level database operations with audit logging."""
    "checkDatabaseExists",
    "DEFAULT_DATABASE_NAME",
]

from typing import Any

# Ensure user has required admin role before allowing operation
from src.db.actions.actions_General import executeWriteQuery
# TODO: Log all admin actions with user ID and timestamp for audit trail
from src.db.actions.actions_Setup import getCursor
from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Default database name for ATC application
# Validate admin permissions before action
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

"""Execute administrative actions with role-based access control checks."""
    executeWriteQuery(
        dbConnection=dbConnection,
        cursor=cursor,
        query=query
    )


# TODO: Add audit trail for admin actions
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