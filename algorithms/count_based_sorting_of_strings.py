# Consider the following motivating application:
# Suppose that a highway engineer sets up a device
# that records the license plate numbers of all
# vehicles using a busy highway for a given period
# of time and wants to know the number of different
# vehicles that used the highway

def get_licence_plate_alphabet():
  alphabet = { str(i): i for i in range(10) }
  for let in range(ord('A'), ord('Z') + 1):
    alphabet[chr(let)] = 10 + let - ord('A')
  return alphabet

def least_significant_digit(array):
  alphabet = get_licence_plate_alphabet()
  # reverse direction
  for s in range(len(array[0]) - 1, -1, -1):
    # count
    counts = [0 for x in range(len(alphabet) + 1)]
    for string in array:
      char = string[s]
      counts[alphabet[char] + 1] += 1

    # cumulate counts
    for i in range(1, len(counts)):
      counts[i] += counts[i-1]

    # distribute
    aux = [None for x in range(len(array))]
    for string in array:
      char = string[s]
      index = alphabet[char]
      aux[counts[index]] = string
      counts[index] += 1

    # copy back
    array = [x for x in aux]
  return array


def most_signficant_digit(array):
  alphabet = get_licence_plate_alphabet()

  # sort by first letter
  # then recurse using hi to lo strategy
  msd_sort(array, 0, len(array), 0, alphabet)
  return array


def insertion_sort(array, lo, hi, d):
  less = lambda string1, string2, d: string1[d:] < string2[d:]

  # for each string find the smallest
  # and swap with current position
  for i in range(lo, hi):
    smallest = array[i]
    smallest_i = i
    for j in range(i + 1, hi):
      if less(array[j], smallest, d):
        smallest_i = j
        smallest = array[j]
    # swap
    array[i], array[smallest_i] = smallest, array[i]
  return array

def msd_sort(array, lo, hi, d, alphabet):
  R = len(alphabet)
  counts = [0 for i in range(R+2)]

  if hi - lo <= 10:
    # TODO: insertion sort
    # Insertion sort is critical as each
    # subarray requires initializing
    # the counts array of size R
    # if ascii -> len (2**8) 256
    # if unicode -> len (2**16) 65536
    return insertion_sort(array, lo, hi, d)

  # counts
  for i in range(lo, hi):
    string = array[i]
    if len(string) <= d:
      counts[1] += 1 # end of string
    r = alphabet[string[d]]
    # r + 1 for space for start index
    # r + 1 for space for end of strings
    counts[r + 2] += 1

  # sum start indexes
  for r in range(1, len(counts)):
    counts[r] += counts[r - 1]

  aux = [0 for x in range(len(array))]
  # distribute
  for i in range(lo, hi):
    string = array[i]
    if len(string) <= d:
      x = 0
    else:
      char_code = alphabet[string[d]]
      x = char_code + 1
    start_index = counts[x]
    aux[start_index + lo] = string
    counts[x] += 1

  # copy back
  for i in range(lo, hi):
    array[i] = aux[i]

  # sort next char in each subarray
  for i in range(1, len(counts) - 1):
    lo = counts[i]
    hi = counts[i + 1]
    msd_sort(array, lo, hi, d + 1, alphabet)


def three_way_quick_sort_msd(array):
  print('three_way_quick_sort_msd', array)
  d = 0
  lo = 0
  hi = len(array)
  three_way(array, lo, hi, d)
  print(array)
  return array

def three_way(array, lo, hi, d):
  if hi - lo <= 1 or d > len(array[lo]) - 1:
    if lo < len(array):
      print('lo, hi, array[lo-1], array[lo-1][:d], d', lo, hi, array[lo], array[lo][:d], d)
    else:
      print('end', lo)
    return
  print('three_way', lo, hi)
  pivot_start, pivot_end = quick_sort(array, lo, hi, d)
  print('enqueue l', lo, pivot_start)
  three_way(array, lo, pivot_start, d)
  print('enqueue c', pivot_start, pivot_end)
  three_way(array, pivot_start, pivot_end, d + 1)
  print('enqueue r', pivot_end, hi)
  three_way(array, pivot_end, hi, d)

  return array

def quick_sort(array, lo, hi, d):
  # print('sort', lo, hi, array[lo:hi])
  pivot = array[lo][d]
  pivot_len = 0
  j = lo + 1
  while j < hi:
    string = array[j]
    char = string[d]
    if char <= pivot:
      # jump over char
      pivot_lo = j - 1 - pivot_len
      array[pivot_lo], array[j] = array[j], array[pivot_lo]
      if char == pivot:
        pivot_len += 1
      j += 1
    else:
      # send char to back
      array[j], array[hi - 1] = array[hi - 1], array[j]
      hi -= 1
  s, e = j - 1 - pivot_len, j
  # print(s,e)
  return s, e

def quick_sort2(array, lo, hi, d):
  pivot = array[lo][d]
  pivot_start = lo
  pivot_len = 0
  for j in range(pivot_start + 1, hi):
    string = array[j]
    char = string[d]
    if char <= pivot:
      if pivot_start < j:
        # swap
        next_hi = pivot_start + pivot_len + 1
        array[next_hi], array[j] = string, array[next_hi]
        array[next_hi], array[pivot_start + 1] = array[pivot_start + 1], array[next_hi]
      if char == pivot:
        pivot_len += 1
      else:
        pivot_start += 1

  array[pivot_start], array[lo] = array[lo], array[pivot_start]
  s, e = pivot_start, pivot_start + pivot_len + 1
  return s, e

array = ['5', '8', '4', '7', '3', '6', '2']

copy = lambda x: [y for y in x]

# assert quick_sort(copy(array), 0, len(array), 0) == (3, 4)
# assert quick_sort(copy(array), 1, 3, 0) == (2, 3)
# assert three_way_quick_sort_msd(copy(array)) == ['2', '3', '4', '5', '6', '7', '8']

array = ['5', '4', '8', '5', '7', '3', '6', '5', '2']
assert quick_sort(copy(array), 0, len(array), 0) == (3, 6)
assert three_way_quick_sort_msd(copy(array)) == ['2', '3', '4', '5', '5', '5', '6', '7', '8']


array = [
  '5b',
  '4a',
  '8c',
  '7f',
  '6d',
  '5a',
  '3e',
  '6d',
  '5e',
  '2h'
]

assert three_way_quick_sort_msd(copy(array)) == ['2h', '3e', '4a', '5a', '5b', '5e', '6d', '6d', '7f', '8c']

array = [
  '4PGC938',
  '2IYE230',
  '3CIO720',
  '1ICK750',
  '1OHV845',
  '4JZY524',
  '1ICK750',
  '3CIO720',
  '1OHV845',
  '1OHV845',
  '2RLA629',
  '2RLA629',
  '3ATW723'
]

expected = [
  '1ICK750',
  '1ICK750',
  '1OHV845',
  '1OHV845',
  '1OHV845',
  '2IYE230',
  '2RLA629',
  '2RLA629',
  '3ATW723',
  '3CIO720',
  '3CIO720',
  '4JZY524',
  '4PGC938'
]

print('lsd')
for i, x in enumerate(least_significant_digit(array)):
  print(x, expected[i])
  assert x == expected[i]

print('msd')
for i, x in enumerate(most_signficant_digit(array)):
  print(x, expected[i])
  assert x == expected[i]

print('3waymsd')
for i, x in enumerate(three_way_quick_sort_msd(array)):
  print(x, expected[i])
  assert x == expected[i]

