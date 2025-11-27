#!/usr/bin/env python3
"""
Module to measure the total execution time of concurrent coroutines.
"""
import asyncio
import time
from typing import Callable, List

# Import wait_n from the previous file
wait_n: Callable[[int, int], asyncio.Future[List[float]]] = \
    __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns the average time per task (total_time / n).

    Args:
        n (int): The number of times wait_random is spawned.
        max_delay (int): The maximum delay used for wait_random.

    Returns:
        float: The average time taken per coroutine execution.
    """
    # 1. Record the starting time
    start_time = time.time()

    # 2. Execute the asynchronous coroutine using asyncio.run()
    # This function blocks until the coroutine is completed.
    asyncio.run(wait_n(n, max_delay))

    # 3. Record the ending time
    end_time = time.time()

    # 4. Calculate the total elapsed time
    total_time = end_time - start_time

    # 5. Return the average time per call
    return total_time / n

if __name__ == '__main__':
    # Example usage (Test provided in the prompt)
    
    n = 5
    max_delay = 9

    # The total time will be roughly equal to the longest delay,
    # demonstrating concurrency. The average is (longest_delay / n).
    average_time = measure_time(n, max_delay)
    print(f"Total tasks (n): {n}")
    print(f"Max individual delay: {max_delay}s")
    print(f"Average time per task: {average_time}")
