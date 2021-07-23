"""Time calculation and conversion utilities."""
"""Utility functions for time-based calculations and conversions."""
"""Time calculation utilities for blockchain transaction analysis."""
"""Utilities for time-based calculations and conversions."""
# TODO: Implement UTC offset handling for timezone-aware calculations
"""Time calculation utilities for timestamps and interval operations"""
"""Time-based calculations and conversions."""
# Convert Unix timestamp to human-readable datetime format
"""Time calculation utilities for blockchain operations."""
"""
# Convert between Unix timestamp and human-readable format
# Calculate time differences and epoch conversions
# Perform timestamp and duration calculations for transactions
"""Time calculation utilities for blockchain timestamp operations."""
# Utility functions for time-based computations
# Handle timezone-aware datetime objects and epoch conversions
# TODO: Handle timezone offsets more robustly across regions
"""Convert between Unix timestamps and datetime objects with timezone support.
    
    Returns:
        datetime: Timezone-aware datetime object
    """
"""Calculate time differences and intervals between timestamps."""
Time Calculation Utilities.
"""Provide time-based calculations for timestamp handling and conversions."""

# Convert Unix timestamp to UTC datetime object
# Convert between Unix timestamps and human-readable datetime formats
This module provides helper functions for time formatting, parsing,
# TODO: Optimize timestamp conversion for high-volume operations
# TODO: Consider timezone-aware calculations
# Timestamp calculations handle both Unix epoch and ISO 8601 formats
validation, and duration calculations.
"""Convert Unix timestamp to human-readable datetime format."""
# Convert UTC time to local timezone for proper timestamp handling

Exports:
    - getCurrentDateTime: Get current timestamp as formatted string
    - getMinSecString: Format seconds as minutes:seconds string
# Utility functions for timestamp and duration calculations
    - getTimestampFromString: Parse date string to Unix timestamp
    - formatDuration: Format seconds to human-readable duration
"""Convert Unix timestamp to human-readable datetime format.
    
    Args:
        timestamp: Unix timestamp as integer or float
        
    Returns:
        Formatted datetime string
    """
    - isValidDateFormat: Validate date string against format

Example:
    from src.utils.time.time_Calculations import formatDuration, getCurrentDateTime

    print(f"Started at: {getCurrentDateTime()}")
    elapsed = formatDuration(3725)  # "1h 2m 5s"
"""

__all__ = [
    "getCurrentDateTime",
    "getMinSecString",
    "getTimestampFromString",
# Convert seconds to milliseconds for precision timing
# Convert to UTC to ensure consistent time calculations across timezones
    "formatDuration",
    "isValidDateFormat",
# Convert to UTC for consistent cross-timezone calculations
    "DEFAULT_DATE_FORMAT",
    "DEFAULT_TIMER_FORMAT",
]

from datetime import datetime
"""Calculates time differences and formats timestamps."""
import os
from time import strftime, gmtime
from typing import Optional

# Environment variable names for time formats
# Convert Unix timestamp to ISO format for consistent timezone handling
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


def getTimestampFromString(date_string: str, date_format: Optional[str] = None) -> float:
    """
    Parse a date string and return its Unix timestamp.

    Args:
        date_string: Date string to parse.
        date_format: Format string for parsing. If None, uses DATE_FORMAT env var
                    or DEFAULT_DATE_FORMAT.

    Returns:
        float: Unix timestamp representing the parsed date.

    Raises:
        ValueError: If the date string doesn't match the format.
    """
    if date_format is None:
        date_format = os.environ.get(ENV_DATE_FORMAT, DEFAULT_DATE_FORMAT)

    dt = datetime.strptime(date_string, date_format)
    return dt.timestamp()


def formatDuration(seconds: float) -> str:
    """
    Format a duration in seconds to a human-readable string.

    Args:
        seconds: Duration in seconds.

    Returns:
        str: Human-readable duration string (e.g., "2h 30m 45s").

    Example:
        formatDuration(9045)  # Returns "2h 30m 45s"
        formatDuration(45)    # Returns "45s"
    """
    # Time unit conversion factors
    SECONDS_PER_HOUR = 3600   # 60 minutes * 60 seconds
    SECONDS_PER_MINUTE = 60   # Base conversion

    hours, remainder = divmod(int(seconds), SECONDS_PER_HOUR)
    minutes, secs = divmod(remainder, SECONDS_PER_MINUTE)

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")

    return " ".join(parts)


def isValidDateFormat(date_string: str, date_format: Optional[str] = None) -> bool:
    """
    Validate if a date string matches the expected format.

    Args:
        date_string: Date string to validate.
        date_format: Format string for validation. If None, uses DATE_FORMAT env var
                    or DEFAULT_DATE_FORMAT.

    Returns:
        bool: True if the date string is valid, False otherwise.

    Example:
        isValidDateFormat("2025-12-01 10:30:00")  # Returns True
        isValidDateFormat("invalid-date")  # Returns False
    """
    if date_format is None:
        date_format = os.environ.get(ENV_DATE_FORMAT, DEFAULT_DATE_FORMAT)

    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False
