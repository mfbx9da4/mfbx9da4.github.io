# https://leetcode.com/problems/jump-game-ii


def solution(nums):
  distance = 0
  next_distance = 0
  jumps = 0
  for i, x in enumerate(nums):
    if i == len(nums) - 1: return jumps
    next_distance = max(i + x, next_distance)
    if distance <= i:
      assert next_distance > i
      distance = next_distance
      jumps += 1


assert solution([2,3,1,1,4]) == 2
assert solution([2,3,0,1,4]) == 2
assert solution([3,0,2,0,4]) == 2
print('all tests passed ✅')