from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        queue=deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        order=[]
        while queue:
            course=queue.popleft()
            order.append(course)
            for next_course in adj[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        if len(order) == numCourses:
            return order
        return []