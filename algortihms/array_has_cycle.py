# Interview for Big Health

from collections import OrderedDict

def has_cycle()

def has_cycle_rec(graph, node, parents = None):
  parents = parents or set()
  parents.add(node)
  for child in graph[node]:
    if child in parents or has_cycle_rec(graph, child, parents):
      return True
  parents.remove(node)
  return False


print('🚴 2 node cycle')
graph = [
  1,
  0
]
assert has_cycle(graph, 0) == True

print('🚴 3 node cycle, no cycle')
graph = [
  1,
  2,
  1
]

assert has_cycle(graph, 0) == True

print('🚴 depth 4 cycle, simple cycle')
graph = [
  1,
  2,
  3,
  0
]
assert has_cycle(graph, 0) == True

print('🚴 depth 4 cycle, simple cycle')
graph = [
  1,
  2,
  3,
  0
]
assert has_cycle(graph, 0) == True

