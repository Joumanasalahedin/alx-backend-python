#!/usr/bin/env python3
"""
coroutine that collects 10 random numbers from an async generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from the async_generator.

    Uses an async comprehension to collect the numbers.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [num async for num in async_generator()]
