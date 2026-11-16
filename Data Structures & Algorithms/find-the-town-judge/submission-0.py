class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score=Counter()
        for a,b in trust:
            score[a] -= 1
            score[b] += 1
        return next((p for p in range(1, n+1) if score[p] == n-1),-1)