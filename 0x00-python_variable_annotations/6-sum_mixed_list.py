#!/usr/bin/env python3

"""
import list from typing
"""
from typing import List

"""
import datatype from typing module
"""
from typing import Union


"""
function which takes a list and returns their sum as float
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    k = 0
    for i in mxd_lst:
      k += i
    return k
