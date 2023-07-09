#!/usr/bin/env python3

"""
import list type from typing module
"""

from typing import List

"""
takes a list of floats as arg and returns sum as float
"""

def sum_list(input_list: List) -> float:
    k = 0
    for i in input_list:
      k += i
    return k

"""
takes one arg which is a list and returns a float which is the sum of the list
"""
