#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """result"""
    square: float = float(v ** 2)
    return (k, square)
