import random

def insertion_sort(array):
  print(array)
  compare_tuples = []
  for i in range(len(array)):
    smallest = array[i]
    smallest_i = i
    for j in range(i + 1, len(array)):
      compare_tuples.append((i, j))
      if array[j] < smallest:
        smallest_i = j
        smallest = array[j]
    # swap
    array[i], array[smallest_i] = smallest, array[i]
  print('len(array), len(compare_tuples)', len(array), len(compare_tuples))
  return array

def insertion_sort2(array):
  print(array)
  compare_tuples = []
  for i in range(len(array)):
    for j in range(i, 0, -1):
      if array[j-1] > array[j]:
        array[j-1], array[j] = array[j], array[j-1]
      else:
        break
      compare_tuples.append((i,j))
  print('len(array), len(compare_tuples)', len(array), len(compare_tuples))
  return array


array = [random.randint(0, 9) for x in range(10)]
print(insertion_sort(list(array)))
print(insertion_sort2(list(array)))

array = list(range(10))
print(insertion_sort(list(array[::-1])))
print(insertion_sort2(list(array[::-1])))
