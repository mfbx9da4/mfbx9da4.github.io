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

# check_all_blocks_satisfy_k(blocks)
# solve()
#   - check
#   - if satisfies => return blocks / 2
#   - else:
#       best_ans = Infinity
#       for all possible cuts:
#           ans = recurse to get number of cuts
#           min(ans, best_ans)
#     return ans


def count_k(rows):
    s = 0
    for row in rows:
        s += row.count(1)
    return s


def satisfies_k(blocks, k):
    for block in blocks:
        if count_k(block) > k:
            return False
    return True


def solve(blocks, k):
    if satisfies_k(blocks, k):
        return blocks // 2
    new_blocks = [x for x in blocks]
    for row_cut in len(width):
        for block in blocks:
            below = [x for i, x in enumerate(block) if i <]
            # above =
            # solve()
            # for col_cut in cols:


H, W, K = read_array()
rows = []
for h in H:
    row = read_array()
    rows.append(row)
blocks = [rows]
solve(blocks, K)
