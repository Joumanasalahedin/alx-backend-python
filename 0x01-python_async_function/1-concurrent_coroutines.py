#!/usr/bin/env python3
"""Contains a method that spawns wait_random n times with a
specified delay between each call."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """

    delay_coroutines = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*delay_coroutines)

    result = []
    for delay in delays:
        inserted = False
        for i in range(len(result)):
            if delay < result[i]:
                result.insert(i, delay)
                inserted = True
                break
        if not inserted:
            result.append(delay)

    return result
