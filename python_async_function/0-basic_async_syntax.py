#!/usr/bin/env python3
"""Module contains function that delays n seconds and then returns n 
"""
import random, asyncio


async def wait_random(max_delay = 10):
    """Function delays for random num seconds

    Args:
        max_delay (int, optional): No. Of seconds to delay

    Returns:
        _type_: num of seconds delayed as float
    """
    secs = random.uniform(0, max_delay)
    sleep = await asyncio.sleep(secs)

    return secs