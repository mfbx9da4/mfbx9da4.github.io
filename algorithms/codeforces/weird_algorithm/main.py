"""
"""


def read_int(): return int(input())


def solve(T):
    while T != 1:
        print(T)
        if T % 2 == 0:
            T = T // 2
        else:
            T = (T * 3) + 1
    print(T)


T = read_int()
solve(T)
