import heapq
from collections import defaultdict
# https://leetcode.com/problems/reconstruct-itinerary/description/

class Solution(object):
  def findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = defaultdict(list)
    edges_visited = {}
    total_edges = 0
    for ticket in tickets:
      edges_visited[tuple(ticket)] = False
      total_edges += 1
      graph[ticket[0]].append(ticket[1])

    for node, edges in graph.items():
      graph[node] = sorted(edges)

    node = "JFK"
    path = [node]
    edges_count = 0
    is_valid = self.find(graph, node, total_edges, path)
    return path

  def find(self, graph, node, total_edges, path):
    edges = graph[node]
    if not len(edges):
      return len(path) - 1 == total_edges
    for j in range(len(edges)):
      child = edges.pop(j)
      path.append(child)
      is_valid = self.find(graph, child, total_edges, path)
      if is_valid:
        return is_valid
      path.pop()
      edges.insert(j, child)
    return False

sol = Solution()
tickets = [["JFK","ATL"],["JFK","SFO"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets = [
  ["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],
  ["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],
  ["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],
  ["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],
  ["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]
]
tickets = [["JFK","A"],["A","B"],["C","A"],["A","C"]]
print(sol.findItinerary(tickets))

