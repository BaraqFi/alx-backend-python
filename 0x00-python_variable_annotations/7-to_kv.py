#!/usr/bin/env python3

"""
import datatype and list from typing module
"""
from typing import Tuple
from typing import Union

"""
takes a string and int/float as args and returns a tuple
"""
def to_kv(k: str, v: [int | float]) -> Tuple[str, float]:
    return (k, v**2)
