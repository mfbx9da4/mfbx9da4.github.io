# Convenience for creating
# https://stackoverflow.com/a/1305663/1376627

class BinaryNode():
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def post_order(node):
  if node is None:
    return
  post_order(node.left)
  post_order(node.right)
  print node.val


def post_order_iter(node):
  stack1 = [node]
  stack2 = []
  seen = {}
  while len(stack1):
    node = stack1.pop(0)
    if node:
      stack1.append(node.left)
      stack1.append(node.right)
      stack2.append(node)
  print [x.val for x in stack2]

def post_order_norm(graph, id):
  if id is None:
    return

  if id in graph:
    node = graph[id]
    post_order_norm(graph, node[0])
    post_order_norm(graph, node[1])
  print id


def in_order(node, nodes=[]):
  if node is None:
    return
  in_order(node.left, nodes)
  nodes.append(node.val)
  in_order(node.right, nodes)
  return nodes

def in_order_iter(node):
  stack = [node]
  stackr = []
  stack2 = []
  seen = {}
  while len(stack):
    while node is not None:
      stack.append(node.left)
      node = node.left
    node = stack.pop(0)
    if node is not None:
      print node.val
      node = node.right

graph = {
  8: (4, 10),
  4: (2, 6),
  10: (9, 20)
}
# post_order_norm(graph, 8)
ref_graph = {}
for key, val in graph.iteritems():
  node = ref_graph.get(key, BinaryNode(key))
  node.left = ref_graph.get(val[0], BinaryNode(val[0]))
  node.right = ref_graph.get(val[1], BinaryNode(val[1]))
  ref_graph[key] = node
  ref_graph[val[0]] = node.left
  ref_graph[val[1]] = node.right
# post_order(ref_graph[8])
# post_order_iter(ref_graph[8])
# print in_order(ref_graph[8])
print in_order_iter(ref_graph[8])
