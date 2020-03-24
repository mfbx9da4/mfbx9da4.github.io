"""
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_array(): return list(map(int, input().split(' ')))


def array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def matrix_to_string(arr, sep=' '): return '[\n' + '\n'.join(
    [sep.join(map(str, row)) for row in arr]) + '\n]'


def solve(string):
    if string != string[::-1]:
        return False
    first = string[0:(len(string) - 1) // 2]
    if first != first[::-1]:
        return False
    second = string[(len(string) + 2) // 2:]
    if second != second[::-1]:
        return False
    return True


string = input()
if solve(string):
    print('Yes')
else:
    print('No')
