import random
# Each row and each column is sorted in asc order
# Find element
# p419

def width(lo, hi):
  return hi[1] - lo[1]

def height(lo, hi):
  return hi[0] - lo[0]


def recurse(matrix, x, lo=None, hi=None):
  """
  TODO: could be improved
  the numbers in the bottom_left will all be greater
  than the lo of the bottom_left quadrant therefore you can
  if x > top_right.hi_val and bottom_left.lo_val < x:
    inspect bottom_left
  else:
    inspect bottom right and top right
  """
  print('CALLED', lo, hi, val(matrix, lo), val(matrix, hi))
  mid = get_mid(lo, hi)
  mid_val = val(matrix, mid)
  if width(lo, hi) == 0 or height(lo, hi) == 0:
    return mid if mid_val == x else -1
  if x < mid_val:
    # top left
    print('top left')
    hi = mid
    return recurse(matrix, x, lo, hi)
  elif x > mid_val:
    dirs = ['top_right', 'bottom_right', 'bottom_left']
    quadrants = [
      top_right(lo, mid, hi),
      bottom_right(lo, mid, hi),
      bottom_left(lo, mid, hi)
    ]
    for i, bounds in enumerate(quadrants):
      lo, hi = bounds
      print(mid_val, dirs[i], lo, hi)
      found = recurse(matrix, x, lo, hi)
      if found != -1:
        return found
    return -1
  else:
    return mid

def top_right(lo, mid, hi):
  lo_r, lo_c = lo
  hi_r, hi_c = hi
  mid_r, mid_c = mid
  lo_r = lo_r
  lo_c = mid_c + 1
  hi_r = mid_r
  hi_c = hi_c
  return (lo_r, lo_c), (hi_r, hi_c)

def bottom_left(lo, mid, hi):
  lo_r, lo_c = lo
  hi_r, hi_c = hi
  mid_r, mid_c = mid
  lo_r = mid_r + 1
  lo_c = lo_c
  hi_r = hi_r
  hi_c = mid_c
  return (lo_r, lo_c), (hi_r, hi_c)

def bottom_right(lo, mid, hi):
  lo_r, lo_c = lo
  hi_r, hi_c = hi
  mid_r, mid_c = mid
  lo_r = mid_r + 1
  lo_c = mid_c + 1
  hi_r = hi_r
  hi_c = hi_c
  return (lo_r, lo_c), (hi_r, hi_c)

def get_mid(lo, hi):
  lo_r, lo_c = lo
  hi_r, hi_c = hi
  mid_r = ((hi_r - lo_r) // 2) + lo_r
  mid_c = ((hi_c - lo_c) // 2) + lo_c
  return mid_r, mid_c

def val(matrix, pos):
  return matrix[pos[0]][pos[1]]

def solve(matrix, x):
  lo = (0, 0) # top left
  hi = (len(matrix) - 1, len(matrix[0]) - 1) # bottom right
  if x == val(matrix, hi):
    return hi
  elif x == val(matrix, lo):
    return lo
  out = recurse(matrix, x, lo, hi)
  print('out', out)
  return out


matrix = [
  [8, 23, 80],
  [15, 24, 83],
  [27, 82, 86],
  [32, 83, 90]
]
assert solve(matrix, 24) == (1, 1)
assert solve(matrix, 32) == (3, 0)
assert solve(matrix, 80) == (0, 2)
assert solve(matrix, 90) == (3, 2)
assert solve(matrix, 15) == (1, 0)

def gen_matrix(rows, cols):
  matrix = []
  for r in range(rows):
    row = []
    matrix.append(row)
    for c in range(cols):
      lo = -1
      if r > 0:
        lo = max(matrix[r - 1][c] + 1, lo)
      if c > 0:
        lo = max(matrix[r][c - 1] + 1, lo)
      if c == 0 and r == 0:
        lo = 0
      percent = (((r+1) * (c+1)) / (rows * cols)) * 100
      hi = random.randint(lo, int(percent))
      num = random.randint(lo, hi)
      row.append(num)
  return matrix

def print_matrix(matrix):
  print(',\n'.join([str(x) for x in matrix]))

matrix = gen_matrix(10, 10)
print_matrix(matrix)
matrix = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  [2, 4, 5, 6, 8, 9, 11, 12, 13, 16],
  [3, 5, 8, 9, 13, 16, 18, 19, 27, 28],
  [4, 8, 9, 10, 14, 23, 27, 29, 30, 32],
  [5, 9, 10, 13, 15, 25, 30, 33, 35, 39],
  [6, 10, 12, 14, 17, 27, 32, 34, 49, 53],
  [7, 11, 16, 23, 28, 31, 40, 41, 52, 56],
  [8, 12, 19, 30, 32, 33, 53, 54, 63, 65],
  [9, 14, 20, 36, 39, 41, 55, 57, 69, 75],
  [10, 15, 24, 37, 42, 51, 64, 66, 74, 86]
]

assert solve(matrix, 4) == (1, 1)
assert solve(matrix, 15) == (4, 4)
