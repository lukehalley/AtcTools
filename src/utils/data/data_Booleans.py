"""
Boolean Conversion Utilities.

This module provides helper functions for converting various types to boolean values,
particularly useful for parsing environment variables and configuration values.
"""

from distutils.util import strtobool
from typing import Union

# Valid truthy string values (case-insensitive)
TRUTHY_VALUES = ('true', 'yes', '1', 'on', 'y')
FALSY_VALUES = ('false', 'no', '0', 'off', 'n')


def strToBool(value: Union[str, bool]) -> bool:
    """
    Convert a string or boolean value to a boolean.

    Handles common string representations of boolean values including:
    - 'true', 'yes', '1', 'on' for True
    - 'false', 'no', '0', 'off' for False

    Args:
        value: The value to convert. Can be a string or boolean.

    Returns:
        bool: The converted boolean value.

    Raises:
        ValueError: If the string cannot be interpreted as a boolean.

    Examples:
        >>> strToBool("true")
        True
        >>> strToBool("no")
        False
        >>> strToBool(True)
        True
    """
    if isinstance(value, bool):
        return value
    return bool(strtobool(value))
