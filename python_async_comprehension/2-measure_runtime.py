#!/usr/bin/env python3
"""
Run time for four parallel comprehensions.
This module defines a coroutine to measure the execution time of running
async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List
# Note: Assuming 1-async_comprehension.py is available in the same directory
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures
    the total execution time.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    # Create a list of four instances of the async_comprehension coroutine
    # Note: async_comprehension returns List[float]
    coroutines = [async_comprehension() for _ in range(4)]

    # Run all four coroutines concurrently using asyncio.gather
    # The results (four lists of 10 floats) are collected, but the focus
    # is on the total time taken.
    await asyncio.gather(*coroutines)

    end_time = time.perf_counter()
    
    # Calculate and return the total runtime
    return end_time - start_time