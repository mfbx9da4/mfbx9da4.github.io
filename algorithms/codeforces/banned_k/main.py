"""
"""
from math import factorial
from collections import defaultdict


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


cache = {}


def fac(x):
    return factorial(x)


def choose_combination(n, r):
    if r > n:
        return 0
    # return int((fac(n) / fac((n - r))) * (1 / fac(r)))
    # return (fac(n) // fac((n - 2)) * (1 / 2))
    # return fac((n // n - 2)) * (1 / 2))
    return (n * (n-1)) // 2


def solve(n, array):
    counts = defaultdict(int)
    for x in array:
        counts[x] += 1
    total_ways = 0
    for x, count in counts.items():
        total_ways += choose_combination(counts[x], 2)
    for k in array:
        ways = choose_combination(counts[k] - 1, 2)
        print(total_ways + ways - choose_combination(counts[k], 2))


N = read_int()
array = read_array()
solve(N, array)
