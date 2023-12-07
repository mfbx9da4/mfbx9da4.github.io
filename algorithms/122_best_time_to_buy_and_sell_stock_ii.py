# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


def solution(nums):
  total = 0
  low_i = 0
  cur_profit = 0
  for i, x in enumerate(nums):
    # if it's lower than the last one -> sell otherwise hold
    if i > 0 and x < nums[i - 1]: 
      total += cur_profit
      low_i = i
      cur_profit = 0
    else:
      cur_profit = nums[i] - nums[low_i]
  total += cur_profit
  return total


assert solution([7,1,5,3,3,3,3,3,3,3,6,4]) == 7
assert solution([1,2,3,4,5]) == 4
assert solution([7,6,4,3,1]) == 0