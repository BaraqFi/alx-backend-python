#!/usr/bin/env python3

"""
import function from typing module
"""

from typing import Callable

"""
takes a float as arg and returns a function that multiplies a float
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """
    return a function
    """
    def mul_func(num: float) -> float:

        """
        multiplies a number by another float number
        """
        return num * multiplier
    return mul_func

