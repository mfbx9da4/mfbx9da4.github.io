"""
1
248618
3
12 10 8
6
100 11 15 9 7 8
4
0 1 1 0
2
0 0
"""


def solve(array):
    k = get_rightmost_k()
    _k = get_leftmost_k()
    if k >= _k:
        return 'YES'
    return 'NO'


T = int(input())

for i in range(T):
    size_array = int(input())
    array = list(map(int, input().split(' ')))
    print(solve(array))
