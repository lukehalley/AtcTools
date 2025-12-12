"""
Logging Setup Module.

This module provides centralized logging configuration for the ATC Tools project.
It sets up a consistent logging format across all modules.

Exports:
    - setupLogging: Initialize and configure the project logger
    - getProjectLogger: Retrieve the configured logger instance
    - getLogLevel: Get logging level from environment
    - LOGGER_NAME: Default logger name constant

Example:
    from src.utils.logging.logging_Setup import setupLogging, getProjectLogger

    setupLogging()
    logger = getProjectLogger()
    logger.info("Application started")
"""

__all__ = [
    "setupLogging",
    "getProjectLogger",
    "getLogLevel",
    "LOGGER_NAME",
    "DEFAULT_LOG_FORMAT",
]

import logging
import os
import sys
from typing import Optional

# Default logger name for the project
LOGGER_NAME = "atc-tools"
DEFAULT_LOG_FORMAT = '%(asctime)s | %(levelname)s | %(message)s'

# Environment variable for log level configuration
ENV_LOG_LEVEL = "LOG_LEVEL"

# Supported log levels mapping
LOG_LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def getLogLevel() -> int:
    """
    Get the logging level from environment variable.

    Reads the LOG_LEVEL environment variable and maps it to a logging constant.
    Defaults to INFO if not set or invalid.

    Returns:
        int: Logging level constant (e.g., logging.INFO).
    """
    level_str = os.environ.get(ENV_LOG_LEVEL, "INFO").upper()
    return LOG_LEVEL_MAP.get(level_str, logging.INFO)


def setupLogging() -> logging.Logger:
    """
    Configure and initialize the project logger.

    Sets up logging with a consistent format including timestamp, level,
    and message. The date format is read from the DATE_FORMAT environment
    variable. Log level can be configured via LOG_LEVEL environment variable.

    Returns:
        logging.Logger: Configured logger instance for the project.

    Environment Variables:
        DATE_FORMAT: Custom date format for log timestamps
        LOG_LEVEL: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logger = logging.getLogger(LOGGER_NAME)

    dateFormat: Optional[str] = os.environ.get("DATE_FORMAT")
    logLevel: int = getLogLevel()

    logging.basicConfig(
        level=logLevel,
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
