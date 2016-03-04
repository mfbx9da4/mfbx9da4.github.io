def update_not_x(k, array, num):
    if k > len(array) - 1 or array[k] == num:
        return 0
    else:
        return 1


def update_count_x(i, array, num):
    if i == 0 or array[i - 1] != num:
        return 0
    else:
        return 1


def solution(num, array):
    """
    Start with two cursors. One at the begginning (i)
    and end (k). Also, start with the zeroed-out counts
    of the left and right sides of the array, ie left
    side is the total number of elements == to x (num),
    right side is the total number of elements != to x.

    Work inward from the outside in with the two cursors,
    decrementing k if the left count is greater than the right
    and otherwise increment i.

    If i and k are equal we have found our equilibrium point.

    Unless the left and right are unbalanced in which case we will
    need to move both the cursors together in one direction to
    equalize them.

    """
    i = 0
    k = len(array)
    count_x = 0
    not_x = 0
    iters = 0

    while i != k or count_x != not_x:

        if count_x > not_x:
            if i == k:
                count_x -= update_count_x(i, array, num)
                i -= 1
            k -= 1
            not_x += update_not_x(k, array, num)
            print iters,'decr k', i, k, count_x, not_x
            iters += 1

        else:
            if i == k:
                not_x -= update_not_x(k, array, num)
                k -= 1
            i += 1
            count_x += update_count_x(i, array, num)
            print iters,'incr i', i, k, count_x, not_x
            iters += 1

    return k

def solution2(x, a):
   k = len(a)
   i = 0
   iters = 0
   while i < k:
        if a[i] == x:
            k -= 1
            print iters
            iters += 1
            while a[k] == x and i < k:
                k -= 1
                print iters
                iters += 1

        i += 1

        print iters
        iters += 1

   return k


assert solution(5, [5, 5, 1, 7, 2, 3, 5]) == 4 and solution2(5, [5, 5, 1, 7, 2, 3, 5]) == 4
print ''
assert solution(5, [4, 4, 4, 4]) == 4 and solution2(5, [4, 4, 4, 4]) == 4
print ''
assert solution(4, [4, 4, 4, 4]) == 0 and solution2(4, [4, 4, 4, 4]) == 0
print ''
assert solution(1, [0, 0, 1, 1]) == 2 and solution2(1, [0, 0, 1, 1]) == 2
print ''
assert solution(0, [0, 0, 1, 1]) == 2 and solution2(0, [0, 0, 1, 1]) == 2
print ''
assert solution(1, [1, 1, 0, 0, 1, 1]) == 2 and solution2(1, [1, 1, 0, 0, 1, 1]) == 2
print ''
assert solution(0, [1, 1, 0, 0, 1, 1]) == 4 and solution2(0, [1, 1, 0, 0, 1, 1]) == 4
