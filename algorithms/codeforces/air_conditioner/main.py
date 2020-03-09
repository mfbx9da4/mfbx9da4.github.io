"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_int_array(): return list(map(int, input().split(' ')))


def int_array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def solve(array, M):
    print('array, M', array, M)


T = read_int()

for i in range(T):
    N, M = read_int_array()
    print('N, M', N, M)
    array = []
    for i in range(N):
        t, l, h = read_int_array()
        array.append({'t': t, 'l': l, 'h': h})
    solve(array, M)
