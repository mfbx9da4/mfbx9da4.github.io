# https://leetcode.com/problems/h-index


def brute(nums):
  best_h = 0
  for i in range(len(nums)):
    count = 0
    for x in nums:
      if x >= i:
        count += 1
    if count >= i:
      best_h = max(i , best_h)
  return best_h

def solution(nums):
  counts = [0 for x in range(len(nums) + 1)]
  for x in nums:
    y = min(x, len(counts) - 1)
    counts[y] += 1
  for i in range(len(counts) - 2, -1, -1):
    counts[i] += counts[i + 1]
  for i in range(len(counts) - 1, -1, -1):
    if counts[i] >= i: 
      return i
  return 0



assert solution([1]) == 1
assert solution([3, 0, 6, 1, 5]) == 3
assert solution([1, 3, 1]) == 1
print('All tests passed ✅')