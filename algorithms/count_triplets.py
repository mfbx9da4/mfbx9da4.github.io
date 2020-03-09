#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def sumTo(n):
    return (n + 1) * (n  / 2)

# Complete the countTriplets function below.
def countTriplets(arr, r):
    cardinality = defaultdict(int)
    # could speed up by generating powers upfront
    if r == 1:
        return int(sum(map(sumTo, range(len(arr) - 1))))
    powers = set()
    all_powers = {1: 0, r: 1}
    greatest_power_val = r
    greatest_power = 1
    # generate all powers
    # if in powers, increment  cardinality

    for i, x in enumerate(arr):
        while x > greatest_power_val:
            greatest_power += 1
            greatest_power_val = r ** greatest_power
            all_powers[greatest_power_val] = greatest_power

        pow = all_powers.get(x)
        is_power = pow is not None

        if is_power:
            powers.add(pow)
            cardinality[pow] += 1
    powers = sorted(powers)
    # print(powers, cardinality)
    streaks = []
    streak = []
    for i in range(len(powers)):
        if len(streak) == 0 or powers[i] == streak[-1] + 1:
            streak.append(powers[i])
        else:
            if len(streak) >= 3:
                streaks.append(streak)
            streak = []
    # edge case last streak

    if len(streak) >= 3: streaks.append(streak)
    count = 0
    for streak in streaks:
        count = len(streak) - 2
        for pow in streak:
            count *= cardinality[pow]
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nr = input().rstrip().split()

    # n = int(nr[0])

    # r = int(nr[1])

    # arr = list(map(int, input().rstrip().split()))

    n = 4
    r = 2
    arr = [1, 2, 2, 4]

    ans = countTriplets(arr, r)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
    print(ans)
