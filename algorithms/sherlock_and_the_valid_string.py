#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the isValid function below.
def isValid(s):
    counts = defaultdict(int)
    for x in s:
        counts[x] += 1
    count_counts = defaultdict(int)
    biggest_count = None
    print(counts)
    for x, count in counts.items():
        count_counts[count] += 1
        if biggest_count is None or count > biggest_count:
            biggest_count = count
        if len(count_counts) > 2:
            return 'NO'
    print('count_counts', count_counts)
    if len(count_counts) == 1:
        return 'YES'
    if count_counts[biggest_count] == 1 and count_counts[biggest_count - 1] > 0:
        return 'YES'
    if count_counts[1] == 1:
        return 'YES'
    return 'NO'



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'aabbc'

    result = isValid(s)
    print(result)
