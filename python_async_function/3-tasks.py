#!/usr/bin/env python3
"""
Module defining a regular function that creates an asyncio.Task.
"""
import asyncio
from typing import Callable, Awaitable

# Import wait_random from the previous file.
# The type hint is used to correctly indicate that wait_random is an async function
wait_random: Callable[[int], Awaitable[float]] = \
    __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task object.

    This function is a regular (synchronous) function. It uses
    asyncio.create_task to wrap the wait_random coroutine, scheduling it
    for concurrent execution on the event loop.

    Args:
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        asyncio.Task: A Task object representing the running coroutine.
    """
    # asyncio.create_task() wraps the coroutine and schedules it to run
    # on the event loop that is currently active (provided by asyncio.run()
    # in the calling scope).
    task = asyncio.create_task(wait_random(max_delay))
    return task

if __name__ == '__main__':
    # Demonstration of how to run the task creator function
    async def test_task(max_delay: int) -> float:
        print(f"Creating task with max_delay={max_delay}...")
        
        # task_wait_random is a regular function, so we call it normally.
        task = task_wait_random(max_delay)
        
        print(f"Task type: {task.__class__}")
        print("Awaiting task completion...")
        
        # We must 'await' the Task object to get the result of the coroutine.
        result = await task
        
        print(f"Task finished with result: {result:.4f}")
        return result

    # Execute the test coroutine
    asyncio.run(test_task(7))
