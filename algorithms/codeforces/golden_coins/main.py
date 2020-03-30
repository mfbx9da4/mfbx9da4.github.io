"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


coins = {
    500: 1000,
    100: 0,
    50: 0,
    10: 0,
    5: 5,
    1: 0
}


def solve(number):
    points = 0
    points += (number // 500) * 1000
    number = number % 500
    points += (number // 5) * 5
    number = number % 5
    return points


T = read_int()

print(solve(T))
