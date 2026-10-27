from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for a,b in zip(words,words[1:]):
            if len(a) > len(b) and a.startswith(b):
                return ""
            for x,y in zip(a,b):
                if x != y:
                    if y not in adj[x]:
                        adj[x].add(y)
                        indegree[y] += 1
                    break
                    
        queue = deque(c for c in indegree if indegree[c] == 0)
        res=[]
        while queue:
            c = queue.popleft()
            res.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return "".join(res) if len(res) == len(adj) else ""

