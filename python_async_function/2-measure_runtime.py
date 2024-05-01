#!/usr/bin/env python3
"""Create a measure_time function"""


from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """result"""
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
