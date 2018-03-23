# Find out whether there is a root betweeen two nodes
# page 253

def solve(graph, node1, node2):
  queue = [(node1, 0)]
  seen = {}
  parent = {node1: None}
  while len(queue):
    node, level = queue.pop(0)
    for child in graph[node]:
      if child not in seen:
        parent[child] = node
        if child == node2:
          path = ''
          par = node2
          while par is not None:
            path = '->' + str(par) + path
            par = parent[par]
          print(path)
          return True
        seen[child] = True
        queue.append((child, level + 1))
  return False

print('2 node cycle')
graph = {
  1: [2, 3],
  2: [1],
  3: [2]
}
assert solve(graph, 1, 3) == True

print('long chain')
graph = {
  1: [2,5,6,7],
  2: [3],
  3: [4, 1],
  4: [1],
  5: [8],
  6: [8],
  7: [8],
  8: []
}
assert solve(graph, 1, 8) == True
