#!/usr/bin/env python3
"""
0-basic_async_syntax.py

An asynchronous coroutine that introduces the basic concepts of async and await.
It waits for a random delay and returns the duration.
"""

import asyncio
import random
from typing import (
    Awaitable,
    Union
)


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait (default is 10).

    Returns:
        float: The actual random delay waited.
    """
    # Generate a random float delay between 0 and max_delay (inclusive)
    # random.uniform is used to get a float value
    delay: float = random.uniform(0, max_delay)

    # Use await asyncio.sleep() to pause the coroutine execution for the
    # generated delay without blocking the entire thread.
    # 
    await asyncio.sleep(delay)

    # Return the actual delay waited
    return delay