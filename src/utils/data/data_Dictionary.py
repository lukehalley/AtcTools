"""
Dictionary Manipulation Utilities.

This module provides helper functions for working with dictionaries,
including ordered dictionary operations and string replacements.
"""

import functools
from collections import OrderedDict
from typing import Any, Dict, Tuple


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
