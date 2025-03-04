"""
Time Calculation Utilities.

This module provides helper functions for time formatting and calculations.
"""

from datetime import datetime
import os
from time import strftime, gmtime
from typing import Optional

# Environment variable names for time formats
ENV_DATE_FORMAT = "DATE_FORMAT"
ENV_TIMER_STR_FORMAT = "TIMER_STR_FORMAT"

# Default formats if environment variables are not set
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_TIMER_FORMAT = "%M:%S"


def getCurrentDateTime() -> str:
    """
    Get the current date and time as a formatted string.

    The format is determined by the DATE_FORMAT environment variable.
    Falls back to DEFAULT_DATE_FORMAT if not set.

    Returns:
        str: Formatted current date and time string.
    """
    date_format: str = os.environ.get(ENV_DATE_FORMAT, DEFAULT_DATE_FORMAT)
    return datetime.now().strftime(date_format)


def getMinSecString(time_seconds: float) -> str:
    """
    Convert seconds to a formatted minutes:seconds string.

    The format is determined by the TIMER_STR_FORMAT environment variable.
    Falls back to DEFAULT_TIMER_FORMAT if not set.

    Args:
        time_seconds: Time duration in seconds.

    Returns:
        str: Formatted time string (e.g., "05:30").
    """
    timer_format: str = os.getenv(ENV_TIMER_STR_FORMAT, DEFAULT_TIMER_FORMAT)
    return strftime(timer_format, gmtime(time_seconds))
