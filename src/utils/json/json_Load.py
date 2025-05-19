"""
JSON Loading Utilities.

This module provides helper functions for loading and parsing JSON files
with proper error handling and type safety.
"""

import json
import os
from typing import Any, Dict, Union


def loadJson(path: str) -> Dict[str, Any]:
    """
    Load and parse a JSON file from the given path.

    Args:
        path: Path to the JSON file to load.

    Returns:
        Dict[str, Any]: Parsed JSON content as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        PermissionError: If the file cannot be read due to permissions.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"JSON file not found: {path}")

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def loadJsonSafe(path: str, default: Union[Dict[str, Any], None] = None) -> Dict[str, Any]:
    """
    Safely load a JSON file, returning a default value on error.

    Args:
        path: Path to the JSON file to load.
        default: Default value to return if loading fails. Defaults to empty dict.

    Returns:
        Dict[str, Any]: Parsed JSON content or default value on error.
    """
    if default is None:
        default = {}

    try:
        return loadJson(path)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return default