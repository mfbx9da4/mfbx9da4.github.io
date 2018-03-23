import random
from timer import Timer
import matplotlib.pyplot as plt

# time_in_secs = .000000007 * (str_length)
max_str_length = 1000000
str_length_range = range(1, max_str_length, max_str_length // 10)
string = 'a'
v1 = []
v2 = []
v3 = []
v4 = []
test_n = 100
letters = [chr(x) for x in range(ord('A'), ord('z'))]
for str_length in str_length_range:
  if str_length % 100 == 0:
    print(str_length)
  a = 'a' * str_length
  b = 'a' * str_length
  rand_a = ''.join([random.choice(letters) for x in range(str_length)])
  rand_b = ''.join([random.choice(letters) for x in range(str_length)])
  with Timer('cmp length ' + str(str_length), print_message=False) as t:
    for i in range(test_n):
      a == b
  v1.append(t.delta)
  with Timer('sub length ' + str(str_length), print_message=False) as t:
    for i in range(test_n):
      a[str_length // 2:]
  v2.append(t.delta)
  with Timer('cmp length rand ' + str(str_length), print_message=False) as t:
    for i in range(test_n):
      a == b
  v3.append(t.delta)
  with Timer('sub length rand' + str(str_length), print_message=False) as t:
    for i in range(test_n):
      a[str_length // 2:]
  v4.append(t.delta)

print('now plotting')
len(v1) and plt.plot(list(str_length_range), v1, label='cmp')
len(v2) and plt.plot(list(str_length_range), v2, label='substr')
len(v3) and plt.plot(list(str_length_range), v3, label='cmp rand')
len(v4) and plt.plot(list(str_length_range), v4, label='substr rand')
plt.ylabel('time (s)')
plt.xlabel('str_length')
plt.legend()
plt.show()
