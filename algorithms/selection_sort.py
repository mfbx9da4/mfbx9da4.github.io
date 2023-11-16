import random


def min_index(i: int, array: list[int]):
    lowest = array[i]
    lowest_i = i
    for i in range(i+1, len(array)):
        if array[i] < lowest:
            lowest = array[i]
            lowest_i = i
    return lowest_i


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def selection_sort(array):
    for i in range(len(array)):
        lowest_i = min_index(i, array)
        swap(array, i, lowest_i)
    return array


def mixer(N=10): return [random.randint(0, N) for _ in range(N)]


array = mixer()
print(selection_sort(array))
