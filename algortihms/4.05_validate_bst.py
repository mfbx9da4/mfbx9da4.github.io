# check binary search tree is a binary search tree
# page 256

def recurse(graph, node, lo, hi):
  if node is None:
    return None
  children = graph.get(node)
  if not children:
    # at a leaf node, return val
    # the node is both the key and the value
    return node
  left = recurse(graph, children[0], lo, node)
  if left == False:
    return False
  right = recurse(graph, children[1], node, hi)
  if right == False:
    return False

  if left is not None and (left > node or left < lo):
    return False
  if right is not None and (right < node or right > hi):
    return False
  if left is not None and right is not None and left > right:
    return False

  # node is valid
  return node

def is_valid_bst(graph, node):
  return True if recurse(graph, node, float('-inf'), float('inf')) else False

print('depth 2 invalid')
graph = {
  7: [3, 8],
  3: [None, 10]
}
assert is_valid_bst(graph, 7) == False
print('simple invalid')
graph = {
  1: [2, 3]
}
assert is_valid_bst(graph, 1) == False
print('simple valid')
graph = {
  2: [1, 3]
}
assert is_valid_bst(graph, 2) == True
print('depth 2 valid, incomplete')
graph = {
  7: [3, 8],
  3: [1, None]
}
assert is_valid_bst(graph, 7) == True
print('depth 3, valid, unbalanced')
graph = {
  7: [3, 8],
  3: [2, None],
  2: [1, None]
}
assert is_valid_bst(graph, 7) == True
print('depth 3, invalid, unbalanced')
graph = {
  7: [3, 8],
  3: [2, None],
  2: [4, None]
}
assert is_valid_bst(graph, 7) == False
