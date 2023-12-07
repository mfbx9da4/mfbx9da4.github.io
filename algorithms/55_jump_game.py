# https://leetcode.com/problems/jump-game/


def solution(nums):
  distance = 0
  for i, x in enumerate(nums):
    if i > distance:
      return False
    distance = max(distance - 1, i + x)
  return True


assert solution([2,3,1,1,4]) == True
assert solution([3,2,1,0,4]) == False
print('All tests passed ✅')