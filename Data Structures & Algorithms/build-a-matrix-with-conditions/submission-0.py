from collections import deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(conditions):
            adj=[[] for _ in range(k+1)]
            in_degree=[0]*(k+1)
            for u,v in conditions:
                adj[u].append(v)
                in_degree[v] += 1
            queue=deque([i for i in range(1,k+1) if in_degree[i] == 0])
            order=[]
            while queue:
                curr=queue.popleft()
                order.append(curr)
                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            return order if len(order) == k else []
        row_order=topoSort(rowConditions)
        col_order=topoSort(colConditions)
        if not row_order or not col_order:
            return []
        row_pos={val: idx for idx, val in enumerate(row_order)}
        col_pos={val:idx for idx,val in enumerate(col_order)}

        matrix=[[0] * k for _ in range(k)]
        for i in range(1,k+1):
            r=row_pos[i]
            c=col_pos[i]
            matrix[r][c] = i
        return matrix

    