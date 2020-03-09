"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_int_array(): return list(map(int, input().split(' ')))


def int_array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def solve(x, y, a, b):
    ans = (y - x) / (a + b)
    if int(ans) == ans:
        return print(int(ans))
    return print(-1)


T = read_int()

for i in range(T):
    x, y, a, b = read_int_array()
    solve(x, y, a, b)
