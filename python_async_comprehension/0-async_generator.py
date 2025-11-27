#!/usr/bin/env python3
"""
0-async_generator module

Contains a coroutine that yields 10 random numbers asynchronously,
waiting 1 second between each yield.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
"""
Asynchronous generator that yields a random float between 0 and 10
every second, for a total of 10 values.

Yields:
    float: A random float number between 0 and 10.
"""
for _ in range(10):
    await asyncio.sleep(1)
    yield random.uniform(0, 10)
