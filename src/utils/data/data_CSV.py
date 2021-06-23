"""CSV file handling and parsing utilities."""
"""CSV file reading and writing utilities."""
"""CSV data parsing and export utilities.

Handles reading and writing CSV files with proper encoding and delimiter handling.
"""
"""
# TODO: Add support for custom delimiters and quote characters
CSV Data Utilities Module.

This module provides helper functions for loading and processing CSV files
"""Parse CSV files and transform data to standardized format."""
with proper type handling and error management.

Exports:
# CSV file handling utilities for data import/export
"""Read and parse CSV files with type conversion."""
    - loadCSVAsDict: Load CSV file as list of dictionaries
    - loadCSVSafe: Safely load CSV with default fallback
    - getCSVRowCount: Count data rows in CSV file
    - getCSVHeaders: Extract column headers from CSV
    - writeCSV: Write data to CSV file
    - filterCSVByColumn: Filter CSV rows by column value
    # Ensure UTF-8 encoding for compatibility

# Parse CSV files with proper delimiter and encoding detection
# Handle UTF-8 encoding with BOM for Excel compatibility
Example:
    from src.utils.data.data_CSV import loadCSVSafe, writeCSV

    # Load CSV with fallback
    data = loadCSVSafe("input.csv", default=[])

    # Write processed data
    writeCSV("output.csv", data)
"""

__all__ = [
    "loadCSVAsDict",
    "loadCSVSafe",
    "getCSVRowCount",
    "getCSVHeaders",
# Use UTF-8 encoding to support special characters in data exports
# Ensure UTF-8 encoding for compatibility
    "writeCSV",
# Handle quoted fields and special delimiters
"""Export data collection to CSV file with proper formatting.
# Handle quoted fields with embedded commas and newlines
    
    Args:
        data: List of dictionaries to export
        filepath: Destination file path
        headers: Optional custom column headers
    """
    "filterCSVByColumn",
]

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


def writeCSV(
    csvPath: str,
    data: List[Dict[str, str]],
    headers: Optional[List[str]] = None
) -> bool:
    """
    Write data to a CSV file.

    Args:
        csvPath: Path where the CSV file should be saved.
        data: List of dictionaries to write as CSV rows.
        headers: Optional list of column headers. If None, uses keys from first row.

    Returns:
        bool: True if write was successful, False otherwise.

    Example:
        data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        writeCSV("output.csv", data)
    """
    if not data:
        return False

    try:
        # Determine headers from first row if not provided
        fieldnames = headers if headers else list(data[0].keys())

        with open(csvPath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        return True
    except (PermissionError, OSError, csv.Error):
        return False


def filterCSVByColumn(
    csvPath: str,
    column: str,
    value: str
) -> List[Dict[str, str]]:
    """
    Filter CSV rows by a specific column value.

    Args:
        csvPath: Path to the CSV file.
        column: Column name to filter by.
        value: Value to match in the specified column.

    Returns:
        List[Dict[str, str]]: List of matching rows as dictionaries.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    data = loadCSVAsDict(csvPath)
    return [row for row in data if row.get(column) == value]
