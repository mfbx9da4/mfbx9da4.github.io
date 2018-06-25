#!/bin/python
# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/torque-and-development/problem

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if n == 1:
      return c_lib
    if c_lib <= c_road:
        return c_lib * n
    cost = 0
    graph = defaultdict(set)
    visited = set()
    for edge in cities:
        v1, v2 = edge
        graph[v1].add(v2)
        graph[v2].add(v1)
    # print(graph)
    for node, children in graph.items():
        if node not in visited:
            # print('lib', node)
            visited.add(node)
            cost += c_lib
            cost = build(node, visited, graph, cost, c_road)
    remaining = n - len(visited)
    cost += remaining * c_lib
    return cost

def build(node, visited, graph, cost, c_road):
    # print('build', node, graph[node], visited)
    for child in graph[node]:
        if child not in visited:
            visited.add(child)
            cost += c_road
            # print('road', node, child, cost)
            cost = build(child, visited, graph, cost, c_road)
    return cost

edges = [[]]
c_lib = 2
c_road = 5
n_nodes = 1
assert roadsAndLibraries(n_nodes, c_lib, c_road, edges) == 2

edges = [
  [1, 2],
  [2, 3],
  [3, 4],
  [1, 3],
  [1, 4]
]
c_lib = 2
c_road = 1
n_nodes = 4
assert roadsAndLibraries(n_nodes, c_lib, c_road, edges) == 5

n_nodes = 3
c_lib = 2
c_road = 1
assert roadsAndLibraries(n_nodes, c_lib, c_road, [[1, 2], [3, 1], [2, 3]]) == 4
edges = [
  [1, 3],
  [3, 4],
  [2, 4],
  [1, 2],
  [2, 3],
  [5, 6]
]
assert roadsAndLibraries(6, 2, 5, edges) == 12

n_nodes = 3
c_lib = 2
c_road = 1
assert roadsAndLibraries(n_nodes, c_lib, c_road, [[1, 2], [3, 1], [2, 3]]) == 4
edges = [
  [1, 3],
  [3, 4],
  [2, 4],
  [1, 2],
  [2, 3],
  [5, 6],
  [7, 6]
]
assert roadsAndLibraries(8, 2, 1, edges) == 9
print('passed all tests')
