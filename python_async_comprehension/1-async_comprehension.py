#!/usr/bin/env python3
"""
1-async_comprehension module

Contains a coroutine that collects 10 random numbers
from async_generator using an async comprehension.
"""

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
"""
Collects 10 random numbers from async_generator using
an asynchronous comprehension.

Returns:
    List[float]: A list of 10 random float numbers.
"""
return [i async for i in async_generator()]
