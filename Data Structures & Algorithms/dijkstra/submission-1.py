import heapq

class Solution:
    def shortestPath(self, n, edges, src):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [float("inf")] * n
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, wt in graph[node]:
                newDist = d + wt

                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(pq, (newDist, nei))

        ans = {}
        for i in range(n):
            if dist[i] == float("inf"):
                ans[i] = -1
            else:
                ans[i] = dist[i]

        return ans