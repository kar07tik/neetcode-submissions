
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
    
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            if i == len(s) -1:
                return True
        
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, len(s)-1)

            for j in range(start,end+1):
                if s[j] == '0':
                    q.append(j)
            farthest = max(farthest,end)
        return False

        