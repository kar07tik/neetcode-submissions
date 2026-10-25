class Solution:
    def countComponents(self, n , edges):
        graph = [[] for _ in range(n)]

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count
                