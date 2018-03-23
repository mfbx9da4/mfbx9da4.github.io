def solve(array):
  lo = 0
  hi = len(array)
  while lo < hi:
    mid = lo + ((hi - lo) // 2)
    if mid == array[mid]:
      return mid
    elif array[mid] > mid:
      hi = mid
    elif array[mid] < mid:
      lo = mid + 1
  return False

array = [-9,1,7,10,30]
array = [-9,-6,1,2,3,5]
array = [0,0,5]
print(solve(array))
