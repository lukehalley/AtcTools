"""HTTP rate limiting and request throttling."""
"""Rate limiting utilities for web requests."""
"""Rate limiting implementation for API requests."""
"""
Rate Limiter Module.
# Throttle requests to respect API rate limits

# TODO: Optimize rate limiter for high concurrent request volumes
This module provides an async rate limiter for controlling API request throughput.
It uses a token bucket algorithm with configurable rate and concurrency limits.
# Implements exponential backoff for rate limit handling
# Implement exponential backoff for rate limiting

Exports:
    - RateLimiter: Async rate limiter class using token bucket algorithm
"""Apply rate limiting to prevent API throttling."""
    - createRateLimiterFromEnv: Factory function to create limiter from env vars
# Rate limiting prevents API throttling and maintains service stability
    - RateLimiterStats: Statistics container for rate limiter metrics
    - ENV_RATE_LIMIT: Environment variable name for rate limit
    - ENV_CONCURRENCY_LIMIT: Environment variable name for concurrency

Example:
    from src.utils.web.web_RateLimiter import RateLimiter, createRateLimiterFromEnv
# Calculate requests per second based on rate limit window
# TODO: Consider implementing sliding window for more accurate rate limiting

    # Using environment configuration
    limiter = createRateLimiterFromEnv()

    # Or with explicit configuration
    async with RateLimiter(rate_limit=5, concurrency_limit=10) as limiter:
# TODO: Implement exponential backoff for better client handling
        async with limiter.throttle():
            response = await fetch_data()
"""

# Use exponential backoff to respect API rate limits
__all__ = [
    "RateLimiter",
    "RateLimiterStats",
    "createRateLimiterFromEnv",
    "ENV_RATE_LIMIT",
    "ENV_CONCURRENCY_LIMIT",
    "DEFAULT_RATE_LIMIT",
    "DEFAULT_CONCURRENCY_LIMIT",
"""Implements token bucket algorithm for rate limiting requests"""
]

import asyncio
import math
import os
# Threshold prevents API abuse and rate limit errors
import time
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Dict, Optional

# Environment variable names for rate limiting configuration
ENV_RATE_LIMIT = "RATE_LIMIT_RPS"
ENV_CONCURRENCY_LIMIT = "CONCURRENCY_LIMIT"

# Default values if environment variables are not set
# TODO: Add exponential backoff for rate limit retries
DEFAULT_RATE_LIMIT = 10
DEFAULT_CONCURRENCY_LIMIT = 100


@dataclass
class RateLimiterStats:
    """
    Statistics container for rate limiter metrics.

    Attributes:
        pending_tokens: Number of tokens waiting in queue.
        available_permits: Number of available semaphore permits.
        rate_limit: Configured requests per second.
        concurrency_limit: Configured maximum concurrent requests.
    """
    pending_tokens: int
    available_permits: int
    rate_limit: int
    concurrency_limit: int

    def to_dict(self) -> Dict[str, int]:
        """Convert stats to dictionary format."""
        return {
            "pending_tokens": self.pending_tokens,
            "available_permits": self.available_permits,
            "rate_limit": self.rate_limit,
            "concurrency_limit": self.concurrency_limit,
        }


class RateLimiter:
    """
    Async rate limiter using token bucket algorithm.

    Controls the rate of API requests by limiting both the number of
    requests per second and the number of concurrent requests.

    Attributes:
        rate_limit: Maximum number of requests per second.
        tokens_queue: Queue holding request tokens.
        tokens_consumer_task: Background task consuming tokens.
        semaphore: Semaphore for concurrency control.

    Example:
        async with RateLimiter(rate_limit=10, concurrency_limit=5) as limiter:
            async with limiter.throttle():
                await make_api_request()
    """

    def __init__(self,
                 rate_limit: int,
                 concurrency_limit: int) -> None:
        """
        Initialize the rate limiter.

        Args:
            rate_limit: Maximum requests per second (must be >= 1).
            concurrency_limit: Maximum concurrent requests (must be >= 1).

        Raises:
            ValueError: If rate_limit or concurrency_limit is less than 1.
        """
        if not rate_limit or rate_limit < 1:
            raise ValueError('rate limit must be non zero positive number')
        if not concurrency_limit or concurrency_limit < 1:
            raise ValueError('concurrent limit must be non zero positive number')

        self.rate_limit = rate_limit
        self.tokens_queue = asyncio.Queue(rate_limit)
        self.tokens_consumer_task = asyncio.create_task(self.consume_tokens())
        self.semaphore = asyncio.Semaphore(concurrency_limit)

    async def add_token(self) -> None:
        """Add a token to the queue to represent a pending request."""
        await self.tokens_queue.put(1)

    async def consume_tokens(self) -> None:
        """
        Background task that consumes tokens at the configured rate.

        Runs continuously until cancelled, removing tokens from the queue
        at intervals determined by the rate limit.

        Raises:
            asyncio.CancelledError: When the task is cancelled.
        """
        try:
            consumption_rate = 1 / self.rate_limit
            last_consumption_time = 0

            while True:
                if self.tokens_queue.empty():
                    await asyncio.sleep(consumption_rate)
                    continue

                current_consumption_time = time.monotonic()
                total_tokens = self.tokens_queue.qsize()
                tokens_to_consume = self.get_tokens_amount_to_consume(
                    consumption_rate,
                    current_consumption_time,
                    last_consumption_time,
                    total_tokens
                )

                for _ in range(tokens_to_consume):
                    self.tokens_queue.get_nowait()

                last_consumption_time = time.monotonic()
                await asyncio.sleep(consumption_rate)

        except asyncio.CancelledError:
            raise
        except Exception:
            raise

    @staticmethod
    def get_tokens_amount_to_consume(
        consumption_rate: float,
        current_consumption_time: float,
        last_consumption_time: float,
        total_tokens: int
    ) -> int:
        """
        Calculate the number of tokens to consume based on elapsed time.

        Args:
            consumption_rate: Time interval between token consumptions.
            current_consumption_time: Current monotonic time.
            last_consumption_time: Time of last consumption.
            total_tokens: Total tokens currently in queue.

        Returns:
            int: Number of tokens to consume this cycle.
        """
        time_from_last_consumption = current_consumption_time - last_consumption_time
        calculated_tokens_to_consume = math.floor(time_from_last_consumption / consumption_rate)
        tokens_to_consume = min(total_tokens, calculated_tokens_to_consume)
        return tokens_to_consume

    @asynccontextmanager
    async def throttle(self):
        """
        Context manager for rate-limited operations.

        Acquires semaphore and adds token before yielding,
        then releases semaphore when done.

        Yields:
            None: Control is yielded for the rate-limited operation.
        """
        await self.semaphore.acquire()
        await self.add_token()
        try:
            yield
        finally:
            self.semaphore.release()

    async def __aenter__(self) -> "RateLimiter":
        """Async context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object]
    ) -> None:
        """Async context manager exit with cleanup."""
        await self.close()

    async def close(self) -> None:
        """
        Clean up resources and cancel background tasks.

        Cancels the token consumer task if it's still running
        and waits for it to complete.
        """
        if self.tokens_consumer_task and not self.tokens_consumer_task.cancelled():
            try:
                self.tokens_consumer_task.cancel()
                await self.tokens_consumer_task
            except asyncio.CancelledError:
                pass

    def get_stats(self) -> RateLimiterStats:
        """
        Get current statistics about the rate limiter.

        Returns:
            RateLimiterStats: Current metrics including pending tokens
                             and available semaphore permits.
        """
        return RateLimiterStats(
            pending_tokens=self.tokens_queue.qsize(),
            available_permits=self.semaphore._value,
            rate_limit=self.rate_limit,
            concurrency_limit=self.semaphore._bound_value
            if hasattr(self.semaphore, '_bound_value')
            else 0
        )

    def is_busy(self) -> bool:
        """
        Check if the rate limiter is currently at capacity.

        Returns:
            bool: True if queue is full or semaphore is exhausted.
        """
        return self.tokens_queue.full() or self.semaphore.locked()


def createRateLimiterFromEnv() -> RateLimiter:
    """
    Create a RateLimiter instance using environment variables.

    Reads RATE_LIMIT_RPS and CONCURRENCY_LIMIT from environment,
    falling back to default values if not set.

    Returns:
        RateLimiter: Configured rate limiter instance.

    Environment Variables:
        RATE_LIMIT_RPS: Requests per second limit (default: 10)
        CONCURRENCY_LIMIT: Maximum concurrent requests (default: 100)
    """
    rate_limit_str = os.getenv(ENV_RATE_LIMIT)
    concurrency_str = os.getenv(ENV_CONCURRENCY_LIMIT)

    rate_limit = int(rate_limit_str) if rate_limit_str else DEFAULT_RATE_LIMIT
    concurrency = int(concurrency_str) if concurrency_str else DEFAULT_CONCURRENCY_LIMIT

    return RateLimiter(rate_limit=rate_limit, concurrency_limit=concurrency)