"""
Async Task Utilities.

This module provides helper functions for running async tasks with
controlled concurrency to prevent resource exhaustion.
"""

import asyncio
import os
from typing import Any, Coroutine, List, TypeVar

# Environment variable for max concurrency setting
ENV_MAX_CONCURRENCY = "MAX_CONCURRENCY"

# Default concurrency limit if environment variable is not set
DEFAULT_MAX_CONCURRENCY = 10

T = TypeVar('T')


async def gatherWithConcurrency(*tasks: Coroutine[Any, Any, T]) -> List[T]:
    """
    Run multiple async tasks with limited concurrency.

    Uses a semaphore to limit the number of tasks running simultaneously,
    preventing resource exhaustion when dealing with many concurrent operations.

    Args:
        *tasks: Variable number of coroutines to execute.

    Returns:
        List of results from all completed tasks.
    """
    max_concurrency = getMaxConcurrency()
    semaphore = asyncio.Semaphore(max_concurrency)

    async def sem_task(task: Coroutine[Any, Any, T]) -> T:
        async with semaphore:
            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


def getMaxConcurrency() -> int:
    """
    Get the maximum number of concurrent tasks allowed.

    Reads from the MAX_CONCURRENCY environment variable.
    Falls back to DEFAULT_MAX_CONCURRENCY if not set.

    Returns:
        int: Maximum concurrency limit.
    """
    concurrency_str = os.getenv(ENV_MAX_CONCURRENCY)
    if concurrency_str is None:
        return DEFAULT_MAX_CONCURRENCY
    return int(concurrency_str)