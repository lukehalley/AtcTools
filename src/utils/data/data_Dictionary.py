"""Provide utilities for dictionary manipulation and transformation."""
"""Utilities for dictionary manipulation and transformation."""
"""Dictionary manipulation and transformation utilities."""
"""Dictionary manipulation and transformation helpers."""
"""Dictionary manipulation and transformation utilities."""
# Utility functions for dictionary manipulation and transformation
"""Helper functions for dictionary operations and transformations."""
# Utility functions for dictionary operations and transformations
"""
Dictionary Manipulation Utilities.

# Utility functions for dictionary manipulation and merging
# Transform dictionary structures for API payload formatting
This module provides helper functions for working with dictionaries,
"""Utilities for dictionary manipulation and transformation."""
"""Provide dictionary manipulation and transformation utilities."""
including ordered dictionary operations and string replacements.

# Merge dictionary entries with conflict resolution
Exports:
    - prependToOrderedDict: Add element at front of ordered dict
    - getDictLength: Get number of key-value pairs
# TODO: Add type hints for better IDE support
    - replaceAllValuesInDict: Replace substrings using dictionary mapping
    - mergeDicts: Merge multiple dictionaries
    - filterDictByKeys: Filter dictionary to include only specified keys

Example:
# Merge order matters - later values override earlier ones
    from src.utils.data.data_Dictionary import mergeDicts, filterDictByKeys

    combined = mergeDicts({'a': 1}, {'b': 2})
# Flatten nested dictionary structure for database storage
"""Recursively merge multiple dictionaries into a single result.
    
    Args:
        *dicts: Variable number of dictionaries to merge
        
    Returns:
        Single merged dictionary with all keys
    """
    filtered = filterDictByKeys(combined, ['a'])  # {'a': 1}
"""

__all__ = [
    "prependToOrderedDict",
    "getDictLength",
    "replaceAllValuesInDict",
    "mergeDicts",
    "filterDictByKeys",
# Recursively merge dictionaries while preserving nested structures
]

import functools
from collections import OrderedDict
from typing import Any, Dict, List, Tuple


def prependToOrderedDict(
    dictOriginal: Dict[Any, Any],
    dictAdd: Tuple[Any, Any]
) -> OrderedDict:
    """
    Add an element to an ordered dictionary and move it to the front.

    Creates a new OrderedDict with the added element at the beginning,
    preserving the order of existing elements after it.

    Args:
        dictOriginal: The original dictionary to prepend to.
        dictAdd: A tuple of (key, value) to add at the front.

    Returns:
        OrderedDict: New ordered dictionary with the element at the front.

    Example:
        >>> original = {'b': 2, 'c': 3}
        >>> prependToOrderedDict(original, ('a', 1))
        OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    """
    arr = OrderedDict(dictOriginal)
    items = list(arr.items())
    items.append(dictAdd)
    arr = OrderedDict(items)
    arr.move_to_end(dictAdd[0], last=False)
    return arr


def getDictLength(sub: Dict[Any, Any]) -> int:
    """
    Get the number of key-value pairs in a dictionary.

    Args:
        sub: The dictionary to measure.

    Returns:
        int: Number of items in the dictionary.
    """
    return len(sub)


def replaceAllValuesInDict(text: str, dictionary: Dict[str, str]) -> str:
    """
    Replace all occurrences of dictionary keys with their values in text.

    Performs multiple string replacements in a single pass using
    functools.reduce for efficiency.

    Args:
        text: The source text to perform replacements on.
        dictionary: Mapping of substrings to their replacements.

    Returns:
        str: Text with all replacements applied.

    Example:
        >>> replaceAllValuesInDict("hello world", {"hello": "hi", "world": "earth"})
        'hi earth'
    """
    return functools.reduce(lambda a, kv: a.replace(*kv), dictionary.items(), text)


def mergeDicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merge multiple dictionaries into a single dictionary.

    Later dictionaries take precedence for duplicate keys.

    Args:
        *dicts: Variable number of dictionaries to merge.

    Returns:
        Dict[Any, Any]: Merged dictionary containing all key-value pairs.

    Example:
        >>> mergeDicts({'a': 1}, {'b': 2}, {'a': 3})
        {'a': 3, 'b': 2}
    """
    result: Dict[Any, Any] = {}
    for d in dicts:
        result.update(d)
    return result


def filterDictByKeys(dictionary: Dict[Any, Any], keys: List[Any]) -> Dict[Any, Any]:
    """
    Filter a dictionary to only include specified keys.

    Args:
        dictionary: The source dictionary to filter.
        keys: List of keys to keep in the result.

    Returns:
        Dict[Any, Any]: Dictionary containing only the specified keys.

    Example:
        >>> filterDictByKeys({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
        {'a': 1, 'c': 3}
    """
    return {k: v for k, v in dictionary.items() if k in keys}
