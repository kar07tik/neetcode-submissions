import heapq
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks=sorted((e,p,i) for i,(e,p) in enumerate(tasks))
        n=len(tasks)
        heap=[]
        res=[]
        time=0
        j=0
        while len(res) < n:
            while j < n and sorted_tasks[j][0] <= time:
                e,p,i = sorted_tasks[j]
                heapq.heappush(heap, (p,i))
                j += 1
            if not heap:
                time=sorted_tasks[j][0]
                continue
            p,i=heapq.heappop(heap)
            time += p
            res.append(i)
        return res