"""
"""
from math import sqrt, ceil


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_int_array(): return list(map(int, input().split(' ')))


def int_array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


def check_all_ones(matrix, w, h, startRow, startCol):
    # if in_range_all_zeroes(w, h, startRow, startCol):
    #     return False
    for row in range(h):
        for col in range(w):
            if matrix[startRow + row][startCol + col] == 0:
                return False
    return True


def count_rectangles(matrix, w, h):
    count = 0
    for row in range(len(matrix) - h + 1):
        num_cols = len(matrix[0])
        for col in range(num_cols - w + 1):
            if check_all_ones(matrix, w, h, row, col):
                count += 1
    # print('count_rectangles, w', w, 'h', h, 'count', count)
    return count


def solve(N, M, K, A, B):
    matrix = []
    for a in A:
        row = []
        for b in B:
            row.append(b * a)
        matrix.append(row)
    # print('N, M, K, A, B', N, M, K, A, B)
    # print('matrix_to_string(matrix)', matrix_to_string(matrix))

    # print('matrix', matrix)
    count = 0
    sqrt_k = ceil(sqrt(K + 1))
    for w in range(1, sqrt_k):
        if K % w == 0:
            h = K // w
            count += count_rectangles(matrix, w, h)
            if w != h:
                count += count_rectangles(matrix, h, w)
    print(count)


N, M, K = read_int_array()
A = read_int_array()
B = read_int_array()
solve(N, M, K, A, B)
