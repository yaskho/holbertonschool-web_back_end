#!/usr/bin/env python3
"""
Async Comprehensions.
This module defines a coroutine that collects 10 random numbers
from an async generator using an asynchronous list comprehension.
"""

from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an async
    list comprehension and returns them.

    Returns:
        List[float]: A list containing the 10 yielded random numbers.
    """
    # Use an asynchronous list comprehension to iterate over the async generator
    # The 'async for' syntax is required inside the comprehension.
    results = [i async for i in async_generator()]
    return results