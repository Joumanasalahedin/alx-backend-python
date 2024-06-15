#!/usr/bin/env python3
"""
coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()

    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)

    end_time = time.time()

    return end_time - start_time
