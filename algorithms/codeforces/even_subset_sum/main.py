"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_int_array(): return list(map(int, input().split(' ')))


def int_array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def solve(array):
    # print('array', array)
    if len(array) == 0:
        return print(-1)
    s = sum(array)
    removal_index = None
    if s % 2 == 0:
        print(len(array))
    else:
        if len(array) == 1:
            return print(-1)
        for i, x in enumerate(array):
            if x % 2 == 1:
                removal_index = i
                break
        if removal_index is None:
            return print(-1)
        print(len(array) - 1)
    # print('removal_index', removal_index)
    indexes = []
    for i, x in enumerate(array):
        if i != removal_index:
            indexes.append(i + 1)
    print(int_array_to_string(indexes))


T = read_int()

for i in range(T):
    N = read_int()
    numbers = read_int_array()
    solve(numbers)
