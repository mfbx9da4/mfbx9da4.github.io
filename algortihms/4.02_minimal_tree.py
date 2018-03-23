# Minimal tree: given a sorted asc array with unique integers
# create a binary search tree of minimal height
# page 253

def solve(array, graph = None, lo=None, hi=None):
  graph = graph or {}
  lo = lo or 0
  hi = hi or len(array)
  length = hi - lo
  # binary tree formation
  # sift up like binary heap?
  # start in the middle bisect left right
  print(array[lo:hi], graph)

  even = length % 2 == 0
  odd = not even
  if length > 3:
    mid = (length // 2) + lo
    root = array[mid]
    root1, graph = solve(array, graph, lo, mid)
    root2, graph = solve(array, graph, mid + 1, hi)
    graph[root] = [root1, root2]
  #   mid = (length // 2) + lo
  #   graph = solve(array, graph, lo, mid)
  #   graph = solve(array, graph, mid, hi)
  elif length == 3:
    root = array[lo + 1]
    graph[array[lo + 1]] = [array[lo], array[lo + 2]]
  elif length == 2:
    root = array[lo + 1]
    graph[array[lo + 1]] = [array[lo], None]
  elif length == 1:
    root = array[lo]
    graph[array[lo]] = [None, None]
  return root, graph

print('simple')
array = [1]
print(solve(array))
array = [0, 1]
print(solve(array))
array = [0, 1, 2]
print(solve(array))
array = [0, 1, 2, 3]
print(solve(array))

print('complex even')
array = [8, 12, 18, 23, 35, 99]
print(solve(array))
print('complex odd')
array = [8, 12, 18, 23, 35, 99, 100]
print(solve(array))
