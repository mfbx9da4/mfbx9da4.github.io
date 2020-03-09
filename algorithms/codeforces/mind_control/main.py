"""
C. Mind Control
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You and your 𝑛−1 friends have found an array of integers 𝑎1,𝑎2,…,𝑎𝑛. You have decided to share it in the following way: All 𝑛 of you stand in a line in a particular order. Each minute, the person at the front of the line chooses either the first or the last element of the array, removes it, and keeps it for himself. He then gets out of line, and the next person in line continues the process.

You are standing in the 𝑚-th position in the line. Before the process starts, you may choose up to 𝑘 different people in the line, and persuade them to always take either the first or the last element in the array on their turn (for each person his own choice, not necessarily equal for all people), no matter what the elements themselves are. Once the process starts, you cannot persuade any more people, and you cannot change the choices for the people you already persuaded.

Suppose that you're doing your choices optimally. What is the greatest integer 𝑥 such that, no matter what are the choices of the friends you didn't choose to control, the element you will take from the array will be greater than or equal to 𝑥?

Please note that the friends you don't control may do their choice arbitrarily, and they will not necessarily take the biggest element available.

Input
The input consists of multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤1000)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains three space-separated integers 𝑛, 𝑚 and 𝑘 (1≤𝑚≤𝑛≤3500, 0≤𝑘≤𝑛−1)  — the number of elements in the array, your position in line and the number of people whose choices you can fix.

The second line of each test case contains 𝑛 positive integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤109)  — elements of the array.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 3500.

Output
For each test case, print the largest integer 𝑥 such that you can guarantee to obtain at least 𝑥
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int_array(): return list(map(int, input().split(' ')))


def read_int(): return int(input())


def solve(n, m, k, array):
    # for first k choose lowest
    # adjust lo / hi
    # next m - k choose worst

    # force choose the worst the ones I can control
    for i in range(k):
        if i == m:
            return max(array[-1], array[0])
        if array[-1] > array[0]:
            array.pop(0)
        else:
            array.pop(-1)

    # unluckily the others choose the best
    for i in range(m - k - 1):
        if array[-1] > array[0]:
            array.pop(-1)
        else:
            array.pop(0)

    # make my choice
    return max(array[-1], array[0])


T = int(input())

for i in range(T):
    n, m, k = read_int_array()
    array = read_int_array()
    print(solve(n, m, k, array))
