import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=[[] for _ in range(n)]
        for (a,b), p in zip(edges,succProb):
            graph[a].append((b,p))
            graph[b].append((a,p))

        best=[0.0]*n
        best[start_node]=1.0
        heap=[(-1.0,start_node)]

        while heap:
            neg,u = heapq.heappop(heap)
            prob = -neg
            if u == end_node:
                return prob
            if prob < best[u]:
                continue
            for v,p in graph[u]:
                cand=prob*p
                if cand > best[v]:
                    best[v]=cand
                    heapq.heappush(heap,(-cand,v))
        return 0.0