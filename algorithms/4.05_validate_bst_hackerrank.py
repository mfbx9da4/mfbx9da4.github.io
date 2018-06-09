# check binary search tree is a binary search tree
# page 256
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

def recurse(node, lo, hi):
  if node is None:
    # at a leaf node, return valid
    return True

  if node.data <= lo or node.data >= hi:
    return False

  # left tree
  left = recurse(node.left, lo, node.data)
  if not left: return False

  # left tree
  right = recurse(node.right, node.data, hi)
  if not right: return False

  # node is valid
  return node

def checkBST(root):
  return bool(recurse(root, float('-inf'), float('inf')))

class node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def buildGraph(ref, root):
  if root is None:
    return
  left, right = ref.get(root, [None, None])
  root_node = node(root)
  root_node.left = buildGraph(ref, left)
  root_node.right = buildGraph(ref, right)
  return root_node


print('depth 2 invalid')
graph = {
  7: [3, 8],
  3: [None, 10]
}
root = buildGraph(graph, 7)
assert checkBST(root) == False
print('simple invalid')
graph = {
  1: [2, 3]
}
root = buildGraph(graph, 1)
print('simple invalid, duplicate')
graph = {
  1: [2, 3]
}
root = buildGraph(graph, 1)
root.left.data = 1
assert checkBST(root) == False
print('simple valid')
graph = {
  2: [1, 3]
}
root = buildGraph(graph, 2)
assert checkBST(root) == True
print('depth 2 valid, incomplete')
graph = {
  7: [3, 8],
  3: [1, None]
}
root = buildGraph(graph, 7)
assert checkBST(root) == True
print('depth 3, valid, unbalanced')
graph = {
  7: [3, 8],
  3: [2, None],
  2: [1, None]
}
root = buildGraph(graph, 7)
assert checkBST(root) == True
print('depth 3, invalid, unbalanced')
graph = {
  7: [3, 8],
  3: [2, None],
  2: [4, None]
}
root = buildGraph(graph, 7)
assert checkBST(root) == False
