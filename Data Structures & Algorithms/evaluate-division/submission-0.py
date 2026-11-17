class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(dict)
        for (u,v), val in zip(equations,values):
            adj[u][v] = val
            adj[v][u] = 1.0 / val
        def dfs(curr,target,visited):
            if curr == target: return 1.0
            visited.add(curr)
            for neighbor, weight in adj[curr].items():
                if neighbor not in visited:
                    res=dfs(neighbor, target,visited)
                    if res != -1.0: return res * weight
            return -1.0
        return [dfs(q[0],q[1],set()) if q[0] in adj and q[1] in adj else -1.0 for q in queries]