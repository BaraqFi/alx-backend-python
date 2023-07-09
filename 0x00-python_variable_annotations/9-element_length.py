#!/usr/bin/env python3

"""
imports multi functions from typing module
"""
from typing import Iterable, Sequence, List, Tuple

"""
function that returns a list
"""
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
