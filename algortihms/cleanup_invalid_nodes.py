
class Node():
  def __init__(self, val=None, children=[]):
    self.val = val
    self.children = children

def solve(graph):
  open_list = [graph.items()[0][1]]
  seen = {}
  while len(open_list):
    node = open_list.pop(0)
    print(node.val)
    valid_children = []
    for child in node.children:
      if child in graph:
        if not child in seen:
          seen[child] = True
          open_list.append(graph[child])
        valid_children.append(child)
      else:
        print 'not found', child
    node.children = valid_children
  return graph

graph = { i: Node(i, [i + 1, i + 2]) for i in range(10) }
solve(graph)
