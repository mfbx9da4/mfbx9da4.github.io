from typing import List
from functools import reduce


def solve(array: List[int]) -> int:
    return reduce(lambda x, y: x + y, array,  0)
