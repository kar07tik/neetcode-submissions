
from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n=numCourses
        adj=[[] for _ in range(n)]
        indeg=[0]*n
        for a,b in prerequisites:
            adj[a].append(b)
            indeg[b] += 1

        pre=[0]*n
        q=deque(i for i in range(n) if indeg[i] == 0)
        while q:
            u=q.popleft()
            for v in adj[u]:
                pre[v] |= pre[u] | (1 << u)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return[bool((pre[v] >> u) & 1) for u,v in queries]