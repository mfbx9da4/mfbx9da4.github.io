import random
from timer import Timer
import matplotlib.pyplot as plt

max_array_length = 10000000
array_length_range = range(1, max_array_length, max_array_length // 10)
v1 = []
v2 = []
v3 = []
v4 = []
test_n = 100
for array_length in array_length_range:
  if array_length % 100 == 0:
    print(array_length)
  array = list(range(array_length))
  with Timer('cmp length ' + str(array_length), print_message=False) as t:
    for i in range(test_n):
      array[0], array[-1] = array[-1], array[0]
  v1.append(t.delta)
  with Timer('sub length ' + str(array_length), print_message=False) as t:
    for i in range(test_n):
      array[0] < array[-1]
  v2.append(t.delta)
  # with Timer('cmp length rand ' + str(array_length), print_message=False) as t:
  #   for i in range(test_n):
  #     a == b
  # v3.append(t.delta)
  # with Timer('sub length rand' + str(array_length), print_message=False) as t:
  #   for i in range(test_n):
  #     a[array_length // 2:]
  # v4.append(t.delta)

print('now plotting')
len(v1) and plt.plot(list(array_length_range), v1, label='swap')
len(v2) and plt.plot(list(array_length_range), v2, label='cmp')
len(v3) and plt.plot(list(array_length_range), v3, label='cmp rand')
len(v4) and plt.plot(list(array_length_range), v4, label='substr rand')
plt.ylabel('time (s)')
plt.xlabel('array_length')
plt.legend()
plt.show()
