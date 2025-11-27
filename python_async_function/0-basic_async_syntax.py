#!/usr/bin/env python3
"""
Module defining the wait_random coroutine.
This coroutine introduces basic asynchronous programming concepts
by simulating an I/O-bound task using a random delay.
"""
import asyncio
import random
from typing import List

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait (default is 10).

    Returns:
        float: The actual random delay time waited.
    """
    # Use random.uniform to get a floating-point number in the range [0, max_delay]
    delay = random.uniform(0, max_delay)
    
    # Use 'await' to pause the execution of this coroutine, allowing the event 
    # loop to run other tasks while we wait for the sleep to complete.
    await asyncio.sleep(delay)
    
    return delay

if __name__ == '__main__':
    # Example usage based on the prompt's test case (0-main.py)
    
    async def test_wait_random():
        """Function to test wait_random for demonstration purposes."""
        
        # Test 1: Default max_delay (10)
        print(f"Waiting with default max_delay (10)...")
        result_default = await wait_random()
        print(f"Result (default): {result_default}")
        
        # Test 2: max_delay = 5
        print(f"\nWaiting with max_delay 5...")
        result_5 = await wait_random(5)
        print(f"Result (5): {result_5}")
        
        # Test 3: max_delay = 15
        print(f"\nWaiting with max_delay 15...")
        result_15 = await wait_random(15)
        print(f"Result (15): {result_15}")

    # asyncio.run() executes the top-level coroutine and manages the event loop.
    asyncio.run(test_wait_random())