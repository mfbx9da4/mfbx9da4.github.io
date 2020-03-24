"""
"""

from math import factorial


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


def combine(n, r):
    try:
        return (factorial(n) / factorial(n - r)) * (1 / r)
    except:
        return 0


def solve(N, M):
    choose_evens = combine(N, 2)
    choose_odds = combine(M, 2)
    return int(choose_evens + choose_odds)


N, M = read_array()
print(solve(N, M))
