class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        dist=[INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            prev = dist[:]
            for u,v, price in flights:
                if prev[u] != INF and prev[u] + price < dist[v]:
                    dist[v] = prev[u] + price
        return dist[dst] if dist[dst] != INF else -1