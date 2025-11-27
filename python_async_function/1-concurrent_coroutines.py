#!/usr/bin/env python3
"""
1-concurrent_coroutines module
Contains a coroutine wait_n that runs wait_random n times concurrently
and returns a list of the results in the order they complete.
"""

import asyncio
from typing import List
wait_random = import('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
"""
Spawns wait_random n times with the specified max_delay and returns
a list of all delays in the order they complete (ascending order).

Args:
    n (int): Number of times to call wait_random.
    max_delay (int): Maximum delay to pass to wait_random.

Returns:
    List[float]: List of delay times in the order they finish.
"""
tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
results: List[float] = []
for coro in asyncio.as_completed(tasks):
    result = await coro
    results.append(result)
return results
