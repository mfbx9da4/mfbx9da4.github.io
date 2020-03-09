"""
"""
from math import sqrt, ceil


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


def solve(N, M, K, A, B):
    L_a = max_ones(A)
    L_b = max_ones(B)
    total = 0
    for p, q in all_divisors(K):
        total += count_recs(p, q, L_a, L_b)
    print(total)
    return total


def all_divisors(K):
    out = []
    sqrt_k = ceil(sqrt(K + 1))
    for p in range(1, sqrt_k):
        if K % p == 0:
            q = K // p
            out.append((p, q))
            if p != q:
                out.append((q, p))
    return out


def max_ones(a):
    L_a = [0]
    seg_i = 0
    for i, j in enumerate(a):
        if j == 1:
            L_a[seg_i] += 1
        elif L_a[seg_i] > 0:
            L_a.append(0)
            seg_i += 1
    return L_a


def count_recs(p, q, L_a, L_b):
    countW = 0
    countH = 0
    for l in L_a:
        if l >= p:
            countW += l-p+1
    for j in L_b:
        if j >= q:
            countH += j-q+1
    return countH*countW


N, M, K = read_array()
A = read_array()
B = read_array()
solve(N, M, K, A, B)
