#!/usr/bin/env python3
"""
Module defining the wait_n coroutine for concurrent execution of wait_random.
"""
import asyncio
from typing import List

# Import wait_random from the previous file.
# Note: In a real project structure, you might use 'from . import wait_random'
# or relative import, but for this standalone test, we assume direct import
# of the function from the base module structure.
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay concurrently.

    The delays are collected and returned in ascending order without using
    list.sort() or sorted(). This is achieved by iterating over the
    completed coroutines using asyncio.as_completed and performing
    a manual insertion sort into the result list.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays: List[float] = []
    
    # 1. Create n instances of the wait_random coroutine
    coros = [wait_random(max_delay) for _ in range(n)]
    
    # 2. Use asyncio.as_completed to process the coroutines as they finish.
    # The iterator yields the results in the order of completion.
    for future in asyncio.as_completed(coros):
        # Await the result of the completed coroutine (the delay value)
        delay = await future
        
        # 3. Insert the delay into the 'delays' list while maintaining order.
        # This acts as an insertion sort, fulfilling the requirement not to use sort().
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        
        # If the delay is the largest so far, append it to the end
        if not inserted:
            delays.append(delay)
            
    return delays

if __name__ == '__main__':
    # Example usage (Test provided in the prompt)
    
    async def test_wait_n():
        """Function to test wait_n for demonstration purposes."""
        
        print("Testing wait_n(5, 5)...")
        results1 = await wait_n(5, 5)
        print(results1)

        print("\nTesting wait_n(10, 7)...")
        results2 = await wait_n(10, 7)
        print(results2)
        
        print("\nTesting wait_n(10, 0)...")
        results3 = await wait_n(10, 0)
        print(results3)


    # asyncio.run() executes the top-level coroutine and manages the event loop.
    asyncio.run(test_wait_n())
    