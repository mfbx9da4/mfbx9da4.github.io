# https://www.hackerrank.com/challenges/how-many-substrings/problem
# n chars
# left and right query
# print number of substrings in inclusive range
# example aab
# output
# a
# aa
# aab
# b
# full string
# example2 aabaab
# output
# aabaab
# aabaa
#  abaab
# aaba
#  abaa
#   baab
# aab
#  aba
#   baa
# aa
#  ab
#   ba
# a
#   b

def solve(parent, substrings, global_counts):
  substrings.add(parent)
  # print('parent', parent, global_counts)
  total = 1

  if parent in global_counts:
    return global_counts[parent]

  if len(parent) < 2:
    return total

  for i in range(2):
    end = (len(parent) - 1) + i
    word = parent[i:end]
    if not word in substrings:
      count = solve(word, substrings, global_counts)
      global_counts[word] = count
      total += count
    else:
      # total += global_counts[word]
      pass

  global_counts[parent] = total
  return total

global_counts = {}
assert solve('aaba', set(), global_counts) == 8
assert solve('aab', set(), global_counts) == 5
print('---')
print(solve('aabaab', set(), global_counts))
assert solve('aabaab', set(), global_counts) == 14
assert solve('aaaaaaaaaaaa', set(), global_counts) == 14

def test_case1():
  string = "qqqqqqqqqqzrzrrzrzrrzrrzrzrrzrzrrzttttttttttttttttttttttttttttttttttttttttttttttttttttttqncpqzcxpbwa"
  assert test([61, 97]) == 349
  assert test([15, 50]) == 447
  assert test([68, 89]) == 63
  assert test([74, 87]) == 14
  assert test([70, 80]) == 11
  assert test([53, 97]) == 437
  assert test([49, 73]) == 25
  assert test([86, 92]) == 26
  assert test([85, 88]) == 7
  assert test([10, 76]) == 1243
  assert test([70, 89]) == 57
  assert test([41, 78]) == 38
  assert test([7, 36]) == 327
  assert test([31, 38]) == 25
  assert test([19, 99]) == 1825
  assert test([91, 91]) == 1
  assert test([86, 98]) == 87
  assert test([21, 66]) == 511
  assert test([91, 91]) == 1
  assert test([49, 90]) == 162
  assert test([44, 51]) == 8
  assert test([12, 66]) == 902
  assert test([86, 91]) == 20
  assert test([42, 56]) == 15
  assert test([6, 46]) == 645
  assert test([52, 71]) == 20
  assert test([10, 72]) == 1143
  assert test([86, 91]) == 20
  assert test([74, 78]) == 5
  assert test([17, 39]) == 191
  assert test([38, 92]) == 314
  assert test([6, 99]) == 2890
  assert test([90, 91]) == 3
  assert test([88, 91]) == 10
  assert test([57, 66]) == 10
  assert test([19, 49]) == 315
  assert test([3, 83]) == 1943
  assert test([42, 75]) == 34
  assert test([69, 70]) == 2
  assert test([95, 96]) == 3
  assert test([77, 98]) == 195
  assert test([76, 87]) == 12
  assert test([59, 80]) == 22
  assert test([47, 90]) == 170
  assert test([68, 90]) == 86
  assert test([4, 51]) == 876
  assert test([89, 92]) == 10
  assert test([69, 79]) == 11
  assert test([0, 44]) == 803
  assert test([49, 94]) == 338
  assert test([27, 43]) == 99
  assert test([40, 47]) == 8
  assert test([42, 75]) == 34
  assert test([68, 69]) == 2
  assert test([59, 89]) == 90
  assert test([62, 79]) == 18
  assert test([34, 37]) == 4
  assert test([52, 93]) == 272
  assert test([31, 60]) == 113
  assert test([19, 35]) == 91
  assert test([14, 46]) == 392
  assert test([93, 96]) == 10
  assert test([62, 82]) == 21
  assert test([74, 84]) == 11
  assert test([44, 56]) == 13
  assert test([96, 96]) == 1
  assert test([80, 92]) == 62
  assert test([41, 72]) == 32
  assert test([80, 99]) == 179
  assert test([17, 39]) == 191
  assert test([0, 85]) == 2238
  assert test([68, 99]) == 335
  assert test([35, 75]) == 41
  assert test([89, 99]) == 64
  assert test([57, 78]) == 22
  assert test([99, 99]) == 1
  assert test([64, 93]) == 188
  assert test([29, 55]) == 143
  assert test([93, 93]) == 1
  assert test([32, 44]) == 36
  assert test([55, 58]) == 4
  assert test([98, 98]) == 1
  assert test([81, 90]) == 34
  assert test([19, 87]) == 923
  assert test([14, 37]) == 203
  assert test([67, 96]) == 252
  assert test([2, 32]) == 347
  assert test([25, 47]) == 169
  assert test([51, 95]) == 367
  assert test([46, 54]) == 9
  assert test([69, 79]) == 11
  assert test([64, 95]) == 250
  assert test([61, 75]) == 15
  assert test([0, 22]) == 193
  assert test([78, 94]) == 106
  assert test([6, 44]) == 587
  assert test([0, 17]) == 114
  assert test([0, 56]) == 1223
  assert test([46, 58]) == 13
  assert test([35, 63]) == 29
