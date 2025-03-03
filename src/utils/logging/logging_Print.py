"""
Logging Print Utilities.

This module provides helper functions for consistent log output formatting.
"""

from src.utils.logging.logging_Setup import getProjectLogger

logger = getProjectLogger()

# Default separator character and length
SEPARATOR_CHAR = "-"
SEPARATOR_LENGTH = 32


def printSeparator(newLine: bool = False) -> None:
    """
    Print a separator line to the log.

    Args:
        newLine: If True, adds a trailing newline to the separator.
    """
    separator = SEPARATOR_CHAR * SEPARATOR_LENGTH
    if newLine:
        separator = f"{separator}\n"

    logger.info(separator)
