#!/usr/bin/ env python3
"""Module contains function that checks async run time

Imports:
    1-concurrent_coroutines: async function to check
    time: time module for getting time elapsed
"""
import time
n_wait = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Function meausres async function runtime

    Args:
        n (int): num of times to run async function
        max_delay (int): max delay of function

    Returns:
        float: return time
    """
    start = time.time()
    await n_wait(n, max_delay)
    end = time.time()

    elapsed = (end - start) / n

    return elapsed
