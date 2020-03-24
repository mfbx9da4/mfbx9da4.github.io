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
    if cache.get(x) is not None:
        return cache[x]
    ans = factorial(x)
    cache[x] = ans
    return ans


def choose_combination(n, r):
    if r > n:
        return 0
    return int((fac(n) / fac((n - r))) * (1 / fac(r)))


def solve(n, array):
    counts = defaultdict(int)
    for x in array:
        counts[x] += 1
    ways_cache = {}
    for k in array:
        if ways_cache.get(k) is not None:
            print(ways_cache[k])
            continue
        ways = 0
        for x, count in counts.items():
            adjusted_count = counts[x]
            if x == k:
                adjusted_count -= 1
            ways += choose_combination(adjusted_count, 2)
        ways_cache[k] = ways
        print(ways)


N = read_int()
array = read_array()
solve(N, array)
