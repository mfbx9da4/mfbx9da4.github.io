"""
A. Non-zero
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Guy-Manuel and Thomas have an array 𝑎 of 𝑛 integers [𝑎1,𝑎2,…,𝑎𝑛]. In one step they can add 1 to any element of the array. Formally, in one step they can choose any integer index 𝑖 (1≤𝑖≤𝑛) and do 𝑎𝑖:=𝑎𝑖+1.

If either the sum or the product of all elements in the array is equal to zero, Guy-Manuel and Thomas do not mind to do this operation one more time.

What is the minimum number of steps they need to do to make both the sum and the product of all elements in the array different from zero? Formally, find the minimum number of steps to make 𝑎1+𝑎2+ … +𝑎𝑛≠0 and 𝑎1⋅𝑎2⋅ … ⋅𝑎𝑛≠0.

Input
Each test contains multiple test cases.

The first line contains the number of test cases 𝑡 (1≤𝑡≤103). The description of the test cases follows.

The first line of each test case contains an integer 𝑛 (1≤𝑛≤100) — the size of the array.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (−100≤𝑎𝑖≤100) — elements of the array .

Output
For each test case, output the minimum number of steps required to make both sum and product of all elements in the array different from zero.
"""


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int_array(): return list(map(int, input().split(' ')))


def read_int(): return int(input())


def solve(array):
    steps = 0
    steps += array.count(0)
    s = sum(array) + steps
    if s == 0:
        steps += 1
    return steps


T = int(input())

for i in range(T):
    n = read_int()
    array = read_int_array()
    print(solve(array))
