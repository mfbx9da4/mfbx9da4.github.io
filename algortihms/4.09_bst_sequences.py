# a bst was created by traversing an array
# given a binary search tree with distinct elements
# page 256
from collections import defaultdict

def solve(graph, root):
  # (1) BFS: create list of each level
  # (2) DFS: for each level generate permuations = {level: [perms]}
  # (3) DFS: for each level maintian path, leaf, print path
  levels = get_levels(graph, root)
  print('levels', levels)
  permuations = generate_permutations(graph, levels)
  print('permuations', permuations)
  print_permutations(permuations)

def print_permutations(permuations):
  root_level = 0
  stack = [(permuations[root_level], root_level)]
  path = []
  seen = set([root_level])
  while len(stack):
    node, level = stack.pop()
    while len(path) > level:
      path.pop() # jumped up
    path.append(node)
    next_level = level + 1
    children = permuations.get(next_level)
    if not children:
      # reached leaf
      print('path', path)
    elif next_level not in seen:
      seen.add(next_level)
      for child in children:
        stack.append((child, next_level))

def generate_permutations(graph, levels):
  permuations = {}
  for level, nodes in levels.items():
    permuations[level] = permute(nodes)
  return permuations

def permute(remaining, path = None, out = None):
  if path is None:
    path = []
  if out is None:
    out = []
  if len(remaining) == 1:
    leaf = path + [remaining[0]]
    out.append(leaf)
    return out
  for i in range(len(remaining)):
    option = remaining.pop(i)
    path.append(option)
    permute(remaining, path, out)
    path.pop()
    remaining.insert(i, option)
  return out

def get_levels(graph, root):
  queue = [(root, 0)]
  levels = defaultdict(list)
  while len(queue):
    node, level = queue.pop(0)
    levels[level].append(node)
    children = graph.get(node, [])
    for child in children:
      queue.append((child, level + 1))
  return levels

print('simple valid')
graph = {
  2: [1, 3]
}
solve(graph, 2)

print('deep valid')
graph = {
  'G': ['E', 'F'],
  'E': ['A', 'B'],
  'F': ['C', 'D']
}
solve(graph, 'G')

print('depth 3, valid, unbalanced')
graph = {
  7: [3, 8],
  3: [2, None],
  2: [1, None]
}
solve(graph, 7)
