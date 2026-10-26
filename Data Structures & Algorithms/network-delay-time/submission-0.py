import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v, t in times:
            graph[u].append((v,t))

        dist={}
        heap=[(0,k)]

        while heap:
            d,u=heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v,t in graph[u]:
                if v not in dist:
                    heapq.heappush(heap,(d+t,v))
        return max(dist.values()) if len(dist) == n else -1