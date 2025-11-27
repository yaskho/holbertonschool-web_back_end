#!/usr/bin/env python3
"""
0-basic_async_syntax module
Contains a coroutine that waits for a random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """""
Waits for a random delay between 0 and max_delay seconds (inclusive)
and returns the actual delay as a float.

Args:
    max_delay (int): Maximum number of seconds to wait (default 10).

Returns:
    float: The actual delay time waited.
    """""
delay: float = random.uniform(0, max_delay)
await asyncio.sleep(delay)
return delay
