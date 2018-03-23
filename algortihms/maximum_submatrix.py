_input = """2
2 2
1 2 -1 -4
4 5
1 2 -1 -4 -20 -8 -3 4 2 1 3 8 10 1 3 -4 -1 1 7 -6
"""

def build_matrix(input):
  lines = input.split('\n')
  n_tests = int(lines[0])
  for t in range(n_tests):
    rows, cols = map(int, lines[(t * 2) + 1].split(' '))
    numbers = map(int, lines[(t * 2) + 2].split(' '))
    print(rows, cols, numbers)
    matrix = []
    for r in range(rows):
      matrix.append([])
      for c in range(cols):
        matrix[r].append(numbers[(r * cols) + c])
    yield matrix

def solve_brute(_input):
  for matrix in build_matrix(_input):
    print matrix
    # for each shape
    # navigate around
    best = None
    max_height = len(matrix) + 1
    max_width = len(matrix[0]) + 1
    for height in range(1, max_height):
      for width in range(1, max_width):
        for row in range(max_height - height):
          for col in range(max_width - width):
            total = 0
            for sub_row in range(row, row + height):
              for sub_col in range(col, col + width):
                total += matrix[sub_row][sub_col]
            if best is None or total > best:
              best = total
              best_sub = (row, col, height, width)
    yield best, best_sub

def solve(_input):
  for matrix in build_matrix(_input):
    print matrix
    # for each shape
    # navigate around
    best = None
    max_height = len(matrix) + 1
    max_width = len(matrix[0]) + 1
    cache = {}
    for height in range(1, max_height):
      for width in range(1, max_width):
        dim = (height, width)
        # we have already calculated this shape
        # submatrix minus the last column
        prev_dim = (height, width - 1)
        cache[dim] = {}
        for row in range(max_height - height):
          for col in range(max_width - width):
            last_col = col + width - 1

            if width == 1:
              # width 1 submatrix has no prev submatrix it can use
              prev_total = 0
            else:
              prev_total = cache[prev_dim][(row, col)]

            last_col_total = 0
            for sub_row in range(row, row + height):
              last_col_total += matrix[sub_row][last_col]

            # the max between cached prev_dim and last col
            # on it's own
            total = max(prev_total + last_col_total, last_col_total)
            cache[dim][(row, col)] = total

            if best is None or total > best:
              best = total
              best_sub = (row, col, height, width)
    yield best, best_sub

print([x for x in solve(_input)])

def max_contiguous_subarray(array):
  solutions = [array[0]]
  global_best = None
  for i in range(1, len(array)):
    x = array[i]
    best = max(x + solutions[i - 1], x)
    solutions.append(best)
    if global_best is None or best > global_best:
      global_best = best
  print(solutions)
  return global_best

# array = [-4, 5, 6, -2, -4, -1, 7]
# print(max_contiguous_subarray(array))
