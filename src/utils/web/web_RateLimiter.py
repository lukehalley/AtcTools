"""
Rate Limiter Module.

This module provides an async rate limiter for controlling API request throughput.
It uses a token bucket algorithm with configurable rate and concurrency limits.
"""

import asyncio
import math
import time
from contextlib import asynccontextmanager
from typing import Optional


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