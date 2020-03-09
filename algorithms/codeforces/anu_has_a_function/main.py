"""
C. Anu Has a Function
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
"""

from itertools import permutations


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int_array(): return list(map(int, input().split(' ')))


def int_array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def f(x, y): return (x | y) - y


def apply_f(arr, i):
    if i == 0:
        return arr[i]
    if i == 1:
        return f(arr[0], arr[1])
    child = apply_f(arr, i - 1)
    return f(child, arr[i])

# 0101
# 1010
# 1111 <<<


def solve(array):
    biggest = -1
    last_i = len(array) - 1
    for ordering in permutations(array):
        ans = apply_f(ordering, last_i)
        if ans > biggest:
            best_ordering = ordering
            biggest = ans
    return best_ordering


def solve_v1(array):
    return sorted(array, reverse=True)


N = int(input())
array = read_int_array()
print(int_array_to_string(solve(array)))
