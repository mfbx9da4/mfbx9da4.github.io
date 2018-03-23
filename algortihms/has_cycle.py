# Interview for Big Health

from collections import OrderedDict

def has_cycle_rec(graph, node, parents = None):
  parents = parents or set()
  parents.add(node)
  for child in graph[node]:
    if child in parents or has_cycle_rec(graph, child, parents):
      return True
  parents.remove(node)
  return False

def has_cycle(graph, node):
  stack = [(node, 0)]
  parents = OrderedDict()
  while len(stack):
    node, level = stack.pop()
    while len(parents) > level:
      parents.popitem()
    parents[node] = True
    for child in graph[node]:
      if child in parents:
        return True
      stack.append((child, level + 1))
  return False

print('2 node cycle')
graph = {
  1: [2],
  2: [1]
}
assert has_cycle_rec(graph, 1) == True
assert has_cycle(graph, 1) == True

print('3 node cycle')
graph = {
  1: [2, 3],
  2: [1],
  3: [2]
}

assert has_cycle_rec(graph, 1) == True
assert has_cycle(graph, 1) == True

print('3 nodes complete, no cycle')
graph = {
  1: [2, 3],
  2: [],
  3: [2]
}
print(graph)
assert has_cycle_rec(graph, 1) == False
assert has_cycle(graph, 1) == False

print('depth 4 cycle, simple cycle')
graph = {
  1: [2],
  2: [3],
  3: [4],
  4: [1]
}
assert has_cycle_rec(graph, 1) == True
assert has_cycle(graph, 1) == True

print('depth 4 cycle, simple cycle')
graph = {
  1: [2],
  2: [3],
  3: [4],
  4: [1]
}
assert has_cycle_rec(graph, 1) == True
assert has_cycle(graph, 1) == True

print('depth 3 cycle, 3 children, no cycle')
graph = {
  0: [1,2,3],
  1: [2,3],
  2: [3,4],
  3: [4],
  4: []
}
assert has_cycle_rec(graph, 0) == False
assert has_cycle(graph, 0) == False
