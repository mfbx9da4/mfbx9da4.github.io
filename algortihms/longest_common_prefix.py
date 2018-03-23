from timer import Timer
import matplotlib.pyplot as plt

class Solution(object):
  def longestCommonPrefix(self, strings):
    if not len(strings):
      return 0
    if len(strings) == 1:
      return len(strings[0])

    # find smallest string
    smallest_i = 0
    smallest = strings[smallest_i]
    for i, string in enumerate(strings):
      if len(string) < len(smallest):
        smallest_i = i
        smallest = string

    lo = 0
    hi = len(smallest)

    # binary search for prefix
    while lo < hi:
      mid = ((hi - lo + 1) // 2) + lo

      smallest_to_mid = smallest[:mid]

      broke = False
      for string in strings:
        if string[:mid] != smallest_to_mid:
          hi = mid - 1
          broke = True
          break

      # prefixes equal
      if not broke:
        lo = mid

    return lo

  def longestCommonPrefix2(self, strings):
    first = strings[0]
    first_i = 0

    for s in range(len(first)):
      for i, string in enumerate(strings):
        if i != first_i and string[s] != first[s]:
          return s
    return len(first)

solution = Solution()

# basic unit tests
print('no prefix')
strings = ['asdf', 'fsa']
assert solution.longestCommonPrefix(strings) == 0
assert solution.longestCommonPrefix2(strings) == 0
print('mid prefix')
strings = ['asdf', 'aspq']
assert solution.longestCommonPrefix(strings) == 2
assert solution.longestCommonPrefix2(strings) == 2
print('whole string')
strings = ['asdf', 'asdf']
assert solution.longestCommonPrefix(strings) == 4
assert solution.longestCommonPrefix2(strings) == 4

suffix_length = 50
calc_suffix_length = lambda prefix_length: (1000 * prefix_length) - prefix_length

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
      assert solution.longestCommonPrefix(strings) == prefix_length
  with Timer(message + 'compare chars') as t:
    for i in range(100):
      assert solution.longestCommonPrefix2(strings) == prefix_length

v1 = []
v2 = []
v3 = []
v4 = []

# benchmark with prefix_range_length
max_prefix_length = 200000
prefix_length_range = range(0, max_prefix_length, max_prefix_length // 10)
for prefix_length in prefix_length_range:
  if prefix_length % 100 == 0:
    print(prefix_length)
  string1 = ('a' * prefix_length) + ('b' * calc_suffix_length(prefix_length))
  string2 = ('a' * prefix_length) + ('c' * calc_suffix_length(prefix_length))
  strings = [string1, string2]
  strings_as_bytes = [bytes(string, 'utf-8') for string in strings]

  # as strings
  # with Timer(print_message=False) as t:
  #   for i in range(10):
  #     assert solution.longestCommonPrefix(strings) == prefix_length
  # v1.append(t.delta)
  # with Timer(print_message=False) as t:
  #   for i in range(10):
  #     assert solution.longestCommonPrefix2(strings) == prefix_length
  # v2.append(t.delta)

  # as bytes
  with Timer(print_message=False) as t:
    for i in range(10):
      assert solution.longestCommonPrefix(strings_as_bytes) == prefix_length
  v3.append(t.delta)
  with Timer(print_message=False) as t:
    for i in range(10):
      assert solution.longestCommonPrefix2(strings_as_bytes) == prefix_length
  v4.append(t.delta)

print('now plotting')
len(v1) and plt.plot(v1, label='binary search, native string comparison')
len(v2) and plt.plot(v2, label='compare characters')
len(v3) and plt.plot(v3, label='binary search, bytes')
len(v4) and plt.plot(v4, label='compare bytes')
plt.ylabel('time (s)')
plt.xlabel('prefix_length')
plt.legend()
plt.show()
