class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        if "0000" in dead: return -1
        queue=deque([("0000",0)])
        visited={"0000"}
        while queue:
            s,t=queue.popleft()
            if s == target: return t
            for i in range(4):
                digit=int(s[i])
                for d in (-1,1):
                    nxt=s[:i] + str((digit + d) % 10) + s[i+1:]
                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt,t+1))
        return -1