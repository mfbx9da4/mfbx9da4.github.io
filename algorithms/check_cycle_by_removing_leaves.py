from collections import DefaultDict

# an acyclic graph will always have a leaf node
# cycle graph will not

def solve(graph, node):
  #   sum to n = ((n + 1) * n / 2)
  #   if edges max is n
  #   if edges  > n * (n-1)/2
  #
  #   the upper bound of M could be in terms of N above
  #
  # For all edges (M + N) => O(N**2):
  #   - count all inward_edges
  #   - keep list of all leaf nodes
  #   - ensure graph edges are sets
  #   - count number of total edges and check against formula
  #
  # while leaf nodes not empty: if acyclic => Θ(N) => O(N)
  #   - remove parent edges and check if parent is now leaf
  #   - if parent is now leaf add to leaf list
  #
  # total runtime:
  #   - theta: O()
  #   - big O: O(M + N) if M > N**2 then O(M) => O(N**2)
  #
  inward_edges = DefaultDict(list)
  leaf_list = []
  queue = [node]
  seen = {}
  # pre processing
  while len(queue):
    node = queue.pop(0)
    children = graph[node]
    # prioritize nodes with least edges first
    if not len(children):
      leaf_list.append(node)
    for child in children:
      inward_edges[child].append(node)
      if not child in seen:
        seen[child] = Truex
        queue.append(child)
  nodes_inspected = 0
  while len(leaf_list):
    nodes_inspected += 1
    node = leaf_list.pop()
    parents = inward_edges[node]
    for parent in parents:
      # remove connections to this leaf
      index = graph[parent].index(node)
      graph[parent].pop(index)
      if len(graph[parent]):
        leaf_list.append(parent)
  if nodes_inspected < len(graph):
    print('no more leaves')
    return True
  print('no cycles')
  return False




graph = {
  1: [2, 3],
  2: [3],
  3: [4],
  4: [1]
}
solve(graph)
