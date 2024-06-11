#!/usr/bin/env python3
"""Asynchronous coroutine to wait for a random delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
