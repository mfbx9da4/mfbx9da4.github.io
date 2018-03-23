_input = """1
3
4
60
70
50
2
"""

def insert_bisect(array, num):
  lo = 0
  hi = len(array)
  while lo < hi:
    mid = lo + ((hi-lo) // 2)
    val = array[mid]
    if num < val:
      hi = mid
    elif num > val:
      lo = mid + 1
    else:
      break # is equal
  array.insert(lo, num) # val at mid is shifted up
  return array

# [2,4] 3
# lo,hi = 0,2; mid, val = 1, 4 => less
# lo,hi = 0,1; mid, val = 0, 2 => greater
# lo,hi = 1,1; => break
#
# [2,3] 3
# lo,hi = 0,2; mid, val = 1, 3 => equal => break
#
# [2,4] 5
# lo,hi = 0,2; mid, val = 1, 4 => greater
# lo,hi = 2,2; => break
#
# [1, 3, 5, 7, 9] 10
# lo,hi = 0,5; mid, val = 2, 5 => greater
# lo,hi = 3,5; mid, val = 3, 7 => greater
# lo,hi = 4,5; mid, val = 4, 9 => greater
# lo,hi = 5,5; => break


def get_median(array):
  mid = len(array) // 2
  return array[mid]

array = []
for num in _input.split('\n'):
  print array
  insert_bisect(array, num)
  print get_median(array)
