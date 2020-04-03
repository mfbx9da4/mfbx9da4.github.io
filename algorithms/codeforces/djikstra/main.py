from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        queue = [(0, K)]
        dists = {K: 0}
        while len(queue):
            # print('queue', queue, dists)
            dist, node = heappop(queue)
            for v, w in graph[node].items():
                if dists.get(v) is None:
                    dists[v] = dist + w
                    heappush(queue, (w + dist, v))
                elif dists.get(v) > w + dist:
                    dists[v] = dist + w
                    heappush(queue, (w + dist, v))
        if len(dists) < N: return -1
        return reduce(lambda p, c: max(p, c), dists.values())
