#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""


import asyncio
from typing import List
from asyncio import gather
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """result"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return completed_delays
