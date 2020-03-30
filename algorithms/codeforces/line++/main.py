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


# pseudocode
# for each x:
#   find_nodes of dist k => add to set
# def find_nodes of dist k:
#   open_list = [(x, 0)]
#   while open_list:
#       if node dist == dist:
#           add_set(node)
#           continue
#       for each child:
#           add(child)
# O(n^2)

def solve(N, x, y):
    initial = [x for x in range(1, N - 1)]
    original_dist = y - x
    for k in range(1, N + 1):
        i = k - 1
        space_before = x >= k
        space_after = y <= (N - (k - 1))
        if space_before:
            initial[i] += 1
        if space_after:
            initial[i] += 1
        if k < original_dist:
            initial[i] -= 1
        print(initial[i])


N, X, Y = read_array()
solve(N, X, Y)
