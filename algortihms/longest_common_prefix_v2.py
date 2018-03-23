from timer import Timer
import matplotlib.pyplot as plt

# https://stackoverflow.com/questions/49353891/why-is-string-comparison-so-fast-in-python


def longestCommonPrefix(smaller, bigger):
  # assumes first arg always smaller
  lo = 0
  hi = len(smaller)

  # binary search for prefix
  while lo < hi:
    # +1 for even lengths
    mid = ((hi - lo + 1) // 2) + lo

    if smaller[:mid] == bigger[:mid]:
      # prefixes equal
      lo = mid
    else:
      # prefixes not equal
      hi = mid - 1

  return lo

def longestCommonPrefix2(smaller, bigger):
  # assumes first arg always smaller
  for p in range(len(smaller)):
    if smaller[p] != bigger[p]:
      return p
  return len(smaller)

# basic unit tests
print('no prefix')
strings = ['asdf', 'fsa']
assert longestCommonPrefix(*strings) == 0
assert longestCommonPrefix2(*strings) == 0
print('mid prefix')
strings = ['asdf', 'aspq']
assert longestCommonPrefix(*strings) == 2
assert longestCommonPrefix2(*strings) == 2
print('diff sizes')
strings = ['aspq', 'asdfgh']
assert longestCommonPrefix(*strings) == 2
assert longestCommonPrefix2(*strings) == 2
print('whole string')
strings = ['asdf', 'asdf']
assert longestCommonPrefix(*strings) == 4
assert longestCommonPrefix2(*strings) == 4

suffix_length = 50
calc_suffix_length = lambda prefix_length: (200 * prefix_length) - prefix_length

# benchmark predifined prefix_lengthes
prefix_lengthes = [4, 21, 256]
prefix_lengthes = [4, 21]
for prefix_length in prefix_lengthes:
  string1 = ('a' * prefix_length) + ('b' * calc_suffix_length(prefix_length))
  string2 = ('a' * prefix_length) + ('c' * calc_suffix_length(prefix_length))
  strings = [string1, string2]
  message = 'Prefix length %d, total_length %d ' % (prefix_length, len(string1))
  with Timer(message + 'binary search') as t:
    for i in range(100):
      assert longestCommonPrefix(*strings) == prefix_length
  with Timer(message + 'compare chars') as t:
    for i in range(100):
      assert longestCommonPrefix2(*strings) == prefix_length

v1 = []
v2 = []
v3 = []
v4 = []

# benchmark with prefix_range_length
max_prefix_length = 1000000
prefix_length_range = range(0, max_prefix_length, max_prefix_length // 10)
for prefix_length in prefix_length_range:
  if prefix_length % 100 == 0:
    print(prefix_length)
  string1 = ('a' * prefix_length) + ('b' * calc_suffix_length(prefix_length))
  string2 = ('a' * prefix_length) + ('c' * calc_suffix_length(prefix_length))
  strings = [string1, string2]
  strings_as_bytes = [bytes(string, 'utf-8') for string in strings]

  # as strings
  with Timer(print_message=False) as t:
    for i in range(10):
      assert longestCommonPrefix(*strings) == prefix_length
  v1.append(t.delta)
  with Timer(print_message=False) as t:
    for i in range(10):
      assert longestCommonPrefix2(*strings) == prefix_length
  v2.append(t.delta)

  # as bytes
  # with Timer(print_message=False) as t:
  #   for i in range(10):
  #     assert longestCommonPrefix(*strings_as_bytes) == prefix_length
  # v3.append(t.delta)
  # with Timer(print_message=False) as t:
  #   for i in range(10):
  #     assert longestCommonPrefix2(*strings_as_bytes) == prefix_length
  # v4.append(t.delta)

print('now plotting')
len(v1) and plt.plot(prefix_length_range, v1, label='binary search, native string comparison')
len(v2) and plt.plot(prefix_length_range, v2, label='compare characters')
len(v3) and plt.plot(prefix_length_range, v3, label='binary search, bytes')
len(v4) and plt.plot(prefix_length_range, v4, label='compare bytes')
plt.title('')
plt.ylabel('time (s)')
plt.xlabel('prefix_length')
plt.legend()
plt.show()
