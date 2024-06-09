#!/usr/bin/env python3
"""Type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple of string and square of the int/float"""
    return (k, v**2)
