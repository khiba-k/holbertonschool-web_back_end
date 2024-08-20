#!/usr/bin/env python3
"""Module contains function async generator
"""
import asyncio
import random


async def async_generator():
    """Function yields certain value between 0 and 10

    Yields:
        _type_: Value between 0 and 10
    """
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1
