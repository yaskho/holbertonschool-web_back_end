#!/usr/bin/env python3
"""
Async Generator.
This module defines a coroutine that loops 10 times, waits 1 second
asynchronously, and then yields a random float between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10 every second.

    The coroutine loops 10 times.
    Each loop:
    1. Asynchronously waits for 1 second using asyncio.sleep(1).
    2. Yields a random floating-point number between 0 and 10.
    
    The function is type-annotated using AsyncGenerator[float, None].
    """
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        
        # Yield a random number between 0 and 10
        yield random.uniform(0, 10)

# The following is for demonstration/testing and not strictly required for the task file itself,
# but it shows how the coroutine is executed.

# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)

# if __name__ == "__main__":
#     import time
#     start_time = time.time()
#     asyncio.run(print_yielded_values())
#     end_time = time.time()
#     print(f"Total execution time: {end_time - start_time:.2f} seconds")