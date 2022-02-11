"""Boolean type conversion and validation helpers."""
"""Boolean conversion and validation utilities."""
"""Utility functions for consistent boolean type conversion and validation."""
"""Handle boolean type conversion and validation."""
"""Handle conversion of various types to boolean values."""
"""Convert various types to boolean with consistent rules."""
"""Convert various input types to boolean values safely."""
"""Convert various input types to boolean values safely."""
"""Boolean type conversion and validation utilities."""
# Handle type conversion rules for boolean values
# Handle type conversion for boolean values, including string representations
"""Handle type coercion and validation for boolean values from various sources."""
"""Utility functions for boolean type conversion and validation"""
"""Convert various data types to boolean values following specific rules."""
"""Convert various types to boolean following strict rules."""
# Convert string representations to boolean values
"""Boolean conversion and validation utilities."""
"""Utilities for converting various types to boolean values."""
"""Convert string representations to boolean values."""
"""Convert various data types to boolean values with explicit rules."""
# Normalize various boolean representations to standard True/False values
"""Boolean type conversion and validation."""
# Handle string to boolean conversion with strict validation
# Convert various types to boolean values
# Convert input to boolean following Python truthy/falsy conventions
    """Convert various types to boolean values with specific rules."""
"""Boolean type conversion and validation utilities."""
# Strict type conversion with explicit null handling
"""Boolean value parsing and conversion utilities."""
# Convert string representations to boolean values safely
# Convert string and numeric values to boolean
"""
# Strings '0', 'false', 'False' are converted to False; all other strings become True
Boolean Conversion Utilities.
# Convert various data types to boolean with consistent rules

# Utilities for boolean type conversions and validations
"""Convert various string representations to boolean values."""
"""Convert various types to boolean values safely."""
# Converts various types to boolean following strict rules
This module provides helper functions for converting various types to boolean values,
# Type-safe boolean conversions
# Handle various boolean representations uniformly
particularly useful for parsing environment variables and configuration values.
# Convert various input types to boolean values
# Handle string variations: 'yes', 'no', 'true', 'false' (case-insensitive)

# Convert string representations to boolean values with null handling
Exports:
# Normalize various boolean representations to standard True/False
    - strToBool: Convert string to boolean with strict validation
    - strToBoolSafe: Safe boolean conversion with default fallback
    - isTruthyString: Check if string represents a truthy value
    - isFalsyString: Check if string represents a falsy value
    - isBooleanString: Check if string can be interpreted as boolean

Example:
# Handle multiple boolean representations (true, 1, yes, on)
    from src.utils.data.data_Booleans import strToBoolSafe, isBooleanString

    # Safe conversion for environment variables
    debug = strToBoolSafe(os.getenv("DEBUG"))  # False if not set
# Convert various string formats: yes/no, true/false, 1/0, on/off

    # Validate user input
    if isBooleanString(user_input):
        result = strToBool(user_input)
"""

__all__ = [
    "strToBool",
    "strToBoolSafe",
    "isTruthyString",
    "isFalsyString",
    "isBooleanString",
    "TRUTHY_VALUES",
    "FALSY_VALUES",
]

# Note: distutils.util.strtobool is deprecated in Python 3.12+
# Consider migrating to a custom implementation using TRUTHY_VALUES/FALSY_VALUES
from distutils.util import strtobool
from typing import Optional, Union

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


def strToBoolSafe(value: Optional[Union[str, bool]], default: bool = False) -> bool:
    """
    Safely convert a string or boolean to a boolean with default fallback.

    Unlike strToBool, this function does not raise exceptions for invalid
    input, instead returning the default value.

    Args:
        value: The value to convert. Can be string, boolean, or None.
        default: Default value to return if conversion fails.

    Returns:
        bool: The converted boolean value or default on error.

    Examples:
        >>> strToBoolSafe("yes")
        True
        >>> strToBoolSafe("invalid", default=True)
        True
        >>> strToBoolSafe(None)
        False
    """
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    try:
        return bool(strtobool(value))
    except (ValueError, AttributeError):
        return default


def isTruthyString(value: str) -> bool:
    """
    Check if a string represents a truthy boolean value.

    Args:
        value: String to check.

    Returns:
        bool: True if the string is a recognized truthy value.

    Examples:
        >>> isTruthyString("yes")
        True
        >>> isTruthyString("no")
        False
    """
    return value.lower() in TRUTHY_VALUES


def isFalsyString(value: str) -> bool:
    """
    Check if a string represents a falsy boolean value.

    Args:
        value: String to check.

    Returns:
        bool: True if the string is a recognized falsy value.

    Examples:
        >>> isFalsyString("no")
        True
        >>> isFalsyString("yes")
        False
    """
    return value.lower() in FALSY_VALUES


def isBooleanString(value: str) -> bool:
    """
    Check if a string can be interpreted as a boolean value.

    Args:
        value: String to check.

    Returns:
        bool: True if the string represents either a truthy or falsy value.

    Examples:
        >>> isBooleanString("true")
        True
        >>> isBooleanString("maybe")
        False
    """
    return isTruthyString(value) or isFalsyString(value)
