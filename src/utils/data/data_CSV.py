"""
CSV Data Utilities Module.

This module provides helper functions for loading and processing CSV files
with proper type handling and error management.
"""

import csv
import os
from typing import List, Dict, Optional


def loadCSVAsDict(csvPath: str) -> List[Dict[str, str]]:
    """
    Load a CSV file and return its contents as a list of dictionaries.

    Each row is converted to a dictionary with column headers as keys.

    Args:
        csvPath: Path to the CSV file to load.

    Returns:
        List[Dict[str, str]]: List of dictionaries representing CSV rows.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        csv.Error: If the file contains invalid CSV data.
    """
    if not os.path.exists(csvPath):
        raise FileNotFoundError(f"CSV file not found: {csvPath}")

    with open(csvPath, 'r', encoding='utf-8') as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, row)) for row in file_data]


def loadCSVSafe(csvPath: str, default: Optional[List[Dict[str, str]]] = None) -> List[Dict[str, str]]:
    """
    Safely load a CSV file, returning a default value on error.

    Args:
        csvPath: Path to the CSV file to load.
        default: Default value to return if loading fails. Defaults to empty list.

    Returns:
        List[Dict[str, str]]: CSV contents or default value on error.
    """
    if default is None:
        default = []

    try:
        return loadCSVAsDict(csvPath)
    except (FileNotFoundError, csv.Error, StopIteration):
        return default


def getCSVRowCount(csvPath: str) -> int:
    """
    Get the number of data rows in a CSV file (excluding header).

    Args:
        csvPath: Path to the CSV file.

    Returns:
        int: Number of data rows in the CSV file.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
    """
    if not os.path.exists(csvPath):
        raise FileNotFoundError(f"CSV file not found: {csvPath}")

    with open(csvPath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f) - 1  # Subtract 1 for header row


def getCSVHeaders(csvPath: str) -> List[str]:
    """
    Get the column headers from a CSV file.

    Args:
        csvPath: Path to the CSV file.

    Returns:
        List[str]: List of column header names.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
    """
    if not os.path.exists(csvPath):
        raise FileNotFoundError(f"CSV file not found: {csvPath}")

    with open(csvPath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return next(reader)
