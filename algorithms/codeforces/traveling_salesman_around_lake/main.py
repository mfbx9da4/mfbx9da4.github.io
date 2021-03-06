"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


def read(): input()


def solve(array, dist):
    total = 0
    biggest = 0
    for i, x in enumerate(array):
        if i == len(array) - 1:
            next_pos = dist + array[0]
        else:
            next_pos = array[i + 1]
        d = next_pos - array[i]
        if d > biggest:
            biggest = d
        total += d
    return total - biggest


K, N = read_array()
array = read_array()
print(solve(array, K))
