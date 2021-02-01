import random


def swap(array, i, j): array[i], array[j] = array[j], array[i]


def insert_left(j, array):
    while j > 0 and array[j] < array[j - 1]:
        swap(array, j, j - 1)
        j -= 1


def sort(array):
    for i in range(1, len(array)):
        insert_left(i, array)
    return array


def mixer(N=10): return [random.randint(0, N) for _ in range(N)]


array = mixer()
print(array)
print(sort(array))
