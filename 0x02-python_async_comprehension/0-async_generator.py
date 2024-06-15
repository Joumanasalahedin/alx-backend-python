#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random numbers
between 0 and 10 with a delay of 1 second between each yield.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates random numbers between 0 and 10.

    The coroutine loops 10 times, each time asynchronously waiting for 1 second
    then yields a random number between 0 and 10.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
