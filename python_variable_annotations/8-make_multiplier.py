#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """result"""
    def multi(value: float) -> float:
        return value * multiplier
    return multi
