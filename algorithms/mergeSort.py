import random


def sort(array):
    print('sort(array)', array)
    # split in half
    # merge each side
    # recombine
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[1] < array[0]:
            swap(array)
        return array
    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)


def swap(array): array[0], array[1] = array[1], array[0]


def merge(a, b):
    print('merge', 'a', a, 'b', b)
    out = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if i == len(a):
            out.append(b[j])
            j += 1
        elif j == len(b):
            out.append(a[i])
            i += 1
        elif a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1

    return out


def random_array(size=10):
    return [random.randint(0, 100) for _ in range(size)]


arr = random_array(9)
print('generated')
print(sort(arr))
