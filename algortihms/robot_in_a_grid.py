# robot can move only right or left
# find path from top right to bottom left

maze = [
  [1,1,1],
  [1,1,0],
  [1,0,0],
  [1,1,1]
]

maze = [
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,0],
  [1,1,0,0,0],
  [1,1,1,1,1]
]

def get_path_recursive(maze):
  """Recursive solution"""
  start = (0, 0) # row, col
  last_r = len(maze) - 1
  last_c = len(maze[0]) - 1 # assume all rows of equal len
  end = (last_r, last_c)

  path = []
  in_bounds = lambda r,c: r <= last_r and c <= last_c
  is_open = lambda r,c: bool(maze[r][c])
  seen = {}

  def recurse(node, path):
    right = (node[0], node[1] + 1)
    down = (node[0] + 1, node[1])

    for move in [right, down]:
      if in_bounds(*move) and is_open(*move):
        if move == end: # found solution
          path.insert(0, move)
          return True

        if seen.has_key(move): # we already checked this guy
          print('dont bother', move)
          continue             # no solution here

        res = recurse(move, path) # dfs
        if res:
          path.insert(0, move)
          return res
    seen[move] = False # no solution

  is_solved = recurse(start, path)
  print(path)
  return is_solved

def get_path(maze):
  """Recursive solution"""
  start = (0, 0) # row, col
  last_r = len(maze) - 1
  last_c = len(maze[0]) - 1 # assume all rows of equal len
  end = (last_r, last_c)

  path = []
  in_bounds = lambda r,c: r <= last_r and c <= last_c
  is_open = lambda r,c: bool(maze[r][c])
  seen = {}
  open_list = [(start, 0)]

  while len(open_list) > 0:
    node, level = open_list.pop(0)
    right = (node[0], node[1] + 1)
    down = (node[0] + 1, node[1])
    print('node', node)

    has_move = False

    for move in [right, down]:
      if in_bounds(*move) and is_open(*move):
        if seen.has_key(move): # we already checked this guy
          print('dont bother', move)
          continue             # no solution here

        has_move = True
        seen[move] = node # points to parent
        if move == end: # found solution
          print('found solution')
          break

        open_list.append((move, level + 1))

    if not has_move:
      print('no move', move)
      seen[move] = False

  path = [end]
  prev = end
  while prev != (0,0):
    prev = seen[prev]
    path.insert(0,prev)

  return path

# print get_path_recursive(maze)
print get_path(maze)
