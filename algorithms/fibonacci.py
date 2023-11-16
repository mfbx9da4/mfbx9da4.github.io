def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    prev0 = 1
    prev1 = 2
    ans = None
    for i in range(3, n+1):
        ans = prev1 + prev0
        prev0 = prev1
        prev1 = i
    return ans


print(fib(4))
