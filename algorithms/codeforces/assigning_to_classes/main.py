# -*- coding: utf-8 -*-
"""
B. Assigning to Classes
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output


It is guaranteed that the sum of 𝑛 over all test cases does not exceed 105.

Output
For each test case, output a single integer, the minimum possible absolute difference between skill levels of two classes of odd sizes.
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int_array(): return list(map(int, input().split(' ')))


def read_int(): return int(input())


# 1 2 3 4 5 6
# 1 2 3  10 11 12
# 1   2 3 10 11 12
def solve(array):
    mid = len(array) // 2
    return array[mid] - array[mid - 1]


def solve_v1(array):
    min_diff = None
    min_i = None
    # . _ . _ . _ .
    # 5 | 1
    for x in range(len(array) // 2):
        i = (x * 2) + 1
        median1i = (i - 1) // 2
        median2i = i + ((len(array) - i - 1) // 2)
        median1 = array[median1i]
        median2 = array[median2i]
        diff = median2 - median1
        if min_i is None or diff < min_diff:
            min_i = i
            min_diff = diff
    return min_diff


T = int(input())

for i in range(T):
    n = read_int()
    array = read_int_array()
    s_array = sorted(array)
    print(solve(s_array))
