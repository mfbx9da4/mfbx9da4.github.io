def as_array(number):
    return list(map(int, [x for x in str(number)]))


def as_int(array):
    return int(''.join(map(str, array)))


def make_odd(num):
    j = -1
    while num[j] % 2 == 0:
        j -= 1
        if abs(j) > len(num):
            return (False, -1)
    return (True, num[:j + 1])


def make_sum_even(num):
    j = None
    for i in range(len(num) - 1):
        x = num[i]
        if x % 2 == 1:
            j = i
            break
    if j is None:
        return (False, -1)
    num.pop(j)
    if len(num) == 0:
        return (False, -1)
    return (True, num)


def solve(number):
    number_as_array = as_array(number)
    # print('number_as_array', number_as_array)
    is_even = number % 2 == 0
    if is_even:
        ok, number_as_array = make_odd(number_as_array)
        # print('number_as_array', number_as_array)
        if not ok:
            return print(-1)
    sum_is_even = sum(number_as_array) % 2 == 0
    if not sum_is_even:
        ok, number_as_array = make_sum_even(number_as_array)
        if not ok:
            return print(-1)
    # print('number_as_array', number_as_array)
    print(as_int(number_as_array))


T = int(input())

for i in range(T):
    digits = int(input())
    number = int(input())
    solve(number)
