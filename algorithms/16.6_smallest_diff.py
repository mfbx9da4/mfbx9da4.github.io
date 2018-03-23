import random

def smallest_diff(arr_a, arr_b):
  i, j = 0, 0
  arr_a = sorted(arr_a)
  arr_b = sorted(arr_b)
  print('sorted', arr_a, arr_b)
  smallest_diff = float('inf')
  smallest_diff_tuple = None
  while i < len(a) and j < len(b):
    val_a = arr_a[i]
    val_b = arr_b[j]
    diff = abs(val_a - val_b)
    print(val_a, val_b)
    if diff < smallest_diff:
      print('smaller', val_a, val_b, diff)
      smallest_diff = diff
      smallest_diff_tuple = (val_a, val_b)

    i_at_end = i == len(arr_a) - 1
    j_at_end = j == len(arr_b) - 1

    if not i_at_end and (j_at_end or val_a < val_b):
      i += 1
    else:
      j += 1
  return smallest_diff_tuple


a = [random.randint(1,100) for x in range(7)]
b = [random.randint(1,100) for x in range(7)]
a, b = [68, 49, 14, 10, 47, 59, 16], [45, 99, 6, 80, 8, 98, 36]
print('original', a, ',', b)
print(smallest_diff(a, b))

