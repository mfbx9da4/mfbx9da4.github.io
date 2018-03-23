# Get the maximal path in 2D grid
# Only down and right


def in_grid_factory(grid):
  def in_grid(coords):
    row, col = coords
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
  return in_grid


def solve(grid):
  queue = [(0,0)]
  seen = {}
  best = {}
  path = {}
  in_grid = in_grid_factory(grid)
  while len(queue):
    row, col = queue.pop(0)
    print(row,col)

    up = (row - 1, col)
    up_sum = best[up] if in_grid(up) else 0
    left = (row, col - 1)
    left_sum = best[left] if in_grid(left) else 0

    if up_sum > left_sum:
      max_sum = up_sum
      path[(row, col)] = up
    else:
      path[(row, col)] = left
      max_sum = left_sum
    best[(row, col)] = max_sum + grid[row][col]

    down = (row + 1, col)
    right = (row, col + 1)

    if not seen.get(down) and in_grid(down):
      seen[down] = True
      queue.append(down)
    if not seen.get(right) and in_grid(right):
      seen[right] = True
      queue.append(right)

  last = (len(grid) - 1, len(grid[0]) - 1)
  best_path = [last]
  node = last
  while node != (0, 0):
    parent = path[node]
    best_path.insert(0, parent)
    node = parent
  return best_path, best[last]


grid = [
  [1,4,4,5],
  [9,3,3,6],
  [1,8,8,5]
]
print solve(grid)
