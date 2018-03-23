# check binary tree is balanced
# page 256

def size(graph, node, depth = 0):
  if node is None:
    return depth - 1, True

  size1, ok1 = size(graph, graph[node][0], depth + 1)
  if not ok1:
    return None, False

  size2, ok2 = size(graph, graph[node][1], depth + 1)
  if not ok2:
    return max(size1, size2), False

  if abs(size2 - size1) > 1:
    return max(size1, size2), False
  return max(size1, size2), True

def is_balanced(graph, root):
  # implement in order traversal
  # if go down level we are going back to fork point
  # if totals for both levels have
  #
  # keep memoized sum of left and right for each node
  # for each level update parent sums +1
  #
  # if leaf node and right branch we can check center
  # total
  queue = [(root, 0)]
  queue2 = []
  total = {}
  prev_level = 0
  prev_fork = root
  while len(queue):
    node, level = queue.pop(0)
    total[prev_fork] = level
    if level < prev_level:
      print('jump up')
    print(node, level)
    total[node] = 0
    for child in graph[node]:
      if child is not None:
        # print('add', child)
        queue.append((child, level + 1))
    prev_level = level

print('unbalanced graph')
graph = {
  'a': ['c', 'b'],
  'b': ['d', None],
  'c': [None, None],
  'd': ['e', None],
  'e': [None, None]
}
# depth, ok = size(graph, 'a')
# assert ok == False
assert is_balanced(graph, 'a') == False
# print('balanced graph, only just')
# graph = {
#   'a': ['b', 'c'],
#   'b': ['d', None],
#   'c': [None, None],
#   'd': [None, None]
# }
# depth, ok = size(graph, 'a')
# assert ok == True

# graph = {
#   1: [2, 3],
#   2: [3, None],
#   3: [4, None],
#   4: [None, None]
# }
# print(size(graph, 1))

# graph = {
#   1: [2, 3],
#   2: [4, None],
#   3: [None, None],
#   4: [None, None]
# }
# print(size(graph, 1))
