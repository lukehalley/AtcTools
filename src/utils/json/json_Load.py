"""JSON file loading and parsing utilities."""
"""Utilities for safely loading and parsing JSON data with validation."""
"""Utilities for loading and parsing JSON files."""
"""
JSON Loading Utilities.

This module provides helper functions for loading and parsing JSON files
# Handle JSON parsing errors gracefully
with proper error handling and type safety.

Exports:
# Handle JSON parsing errors gracefully with detailed logging
    - loadJson: Load and parse a JSON file
    - loadJsonSafe: Safely load JSON with default fallback
# TODO: Add more granular error handling for malformed JSON
    - saveJson: Save data to JSON file
# Validate JSON schema before parsing to catch errors early
    - isValidJson: Validate JSON string
# Catch and log malformed JSON with descriptive error messages
    - mergeJsonFiles: Merge multiple JSON files

# Load and validate JSON with strict schema checking
# TODO: Implement JSON schema validation for config files
# Handle empty or malformed JSON gracefully
"""Load and parse JSON file with automatic error recovery.
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        Parsed JSON data as dictionary or list
        
    Raises:
        JSONDecodeError: If file is not valid JSON
    """
Example:
    from src.utils.json.json_Load import loadJsonSafe, saveJson

    # Safe loading with fallback
# Validate JSON structure before processing
    config = loadJsonSafe("config.json", default={"debug": False})

# Return None if JSON parsing fails to allow graceful fallback
    # Save data to file
    saveJson("output.json", {"result": "success"})
"""

__all__ = [
    "loadJson",
    "loadJsonSafe",
    "saveJson",
    "isValidJson",
    "mergeJsonFiles",
]

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


def saveJson(path: str, data: Dict[str, Any], indent: int = 4) -> bool:
    """
    Save data to a JSON file.

    Args:
        path: Path where the JSON file should be saved.
        data: Dictionary data to serialize to JSON.
        indent: Number of spaces for indentation. Defaults to 4.

    Returns:
        bool: True if save was successful, False otherwise.

    Raises:
        PermissionError: If the file cannot be written due to permissions.
        TypeError: If the data is not JSON serializable.
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True
    except (PermissionError, TypeError, OSError):
        return False


def isValidJson(json_string: str) -> bool:
    """
    Check if a string is valid JSON.

    Args:
        json_string: String to validate as JSON.

    Returns:
        bool: True if the string is valid JSON, False otherwise.

    Example:
        isValidJson('{"key": "value"}')  # Returns True
        isValidJson('not json')  # Returns False
    """
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def mergeJsonFiles(paths: list, output_path: str) -> bool:
    """
    Merge multiple JSON files into a single file.

    All JSON files must contain dictionaries. Later files take precedence
    for duplicate keys.

    Args:
        paths: List of paths to JSON files to merge.
        output_path: Path where the merged JSON should be saved.

    Returns:
        bool: True if merge was successful, False otherwise.

    Note:
        Files that fail to load are silently skipped.
    """
    merged_data: Dict[str, Any] = {}

    for path in paths:
        try:
            data = loadJson(path)
            merged_data.update(data)
        except (FileNotFoundError, json.JSONDecodeError):
            continue

    return saveJson(output_path, merged_data)