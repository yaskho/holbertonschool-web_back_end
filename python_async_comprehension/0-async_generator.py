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
Asynchronous generator that yields 10 random float numbers
between 0 and 10, waiting 1 second between each yield.

Yields:
    float: Random float number between 0 and 10.
"""
for _ in range(10):
    await asyncio.sleep(1)
    yield random.random() * 10
