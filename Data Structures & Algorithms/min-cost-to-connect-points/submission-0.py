from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        INF = float("inf")
        min_dist = [INF] * n
        visited = [False] * n
        min_dist[0] = 0
        total=0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u=i
            visited[u]=True
            total += min_dist[u]

            ux,uy = points[u]
            for v in range(n):
                if not visited[v]:
                    d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                    if d < min_dist[v]:
                        min_dist[v] = d
        return total