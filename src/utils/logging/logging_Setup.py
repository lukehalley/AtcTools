"""
Logging Setup Module.

This module provides centralized logging configuration for the ATC Tools project.
It sets up a consistent logging format across all modules.
"""

import logging
import os
import sys
from typing import Optional

# Default logger name for the project
LOGGER_NAME = "atc-tools"
DEFAULT_LOG_FORMAT = '%(asctime)s | %(levelname)s | %(message)s'


def setupLogging() -> logging.Logger:
    """
    Configure and initialize the project logger.

    Sets up logging with a consistent format including timestamp, level,
    and message. The date format is read from the DATE_FORMAT environment
    variable.

    Returns:
        logging.Logger: Configured logger instance for the project.
    """
    logger = logging.getLogger(LOGGER_NAME)

    dateFormat: Optional[str] = os.environ.get("DATE_FORMAT")

    logging.basicConfig(
        level=logging.INFO,
        format=DEFAULT_LOG_FORMAT,
        stream=sys.stdout,
        datefmt=dateFormat
    )

    return logger


def getProjectLogger() -> logging.Logger:
    """
    Retrieve the project logger instance.

    Returns:
        logging.Logger: The project's logger instance.
    """
    return logging.getLogger(LOGGER_NAME)
