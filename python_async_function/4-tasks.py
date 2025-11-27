#!/usr/bin/env python3
"""
Module defining the task_wait_n coroutine for concurrent execution of tasks.
"""
import asyncio
from typing import List, Callable, Awaitable

# Import the synchronous function that creates an asyncio.Task
task_wait_random: Callable[[int], asyncio.Task] = \
    __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay concurrently
    and returns the list of delays in ascending order.

    The primary difference from wait_n is the use of task_wait_random, which
    returns an already scheduled asyncio.Task object.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay passed to task_wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays: List[float] = []

    # 1. Create n Task objects by calling the synchronous task_wait_random function
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # 2. Use asyncio.as_completed to process the tasks as they finish.
    # The iterator yields the Task objects in the order of completion.
    for completed_task in asyncio.as_completed(tasks):
        # Await the completed Task to get the result (the delay value)
        delay = await completed_task

        # 3. Insertion sort: Insert the delay into the 'delays' list
        # while maintaining ascending order.
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
    
    async def test_task_wait_n():
        """Function to test task_wait_n for demonstration purposes."""
        n = 5
        max_delay = 6
        print(f"Running task_wait_n({n}, {max_delay})...")
        results = await task_wait_n(n, max_delay)
        print(results)
        
    asyncio.run(test_task_wait_n())
