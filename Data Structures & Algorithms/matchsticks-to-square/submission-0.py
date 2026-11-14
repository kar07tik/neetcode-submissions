class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total % 4 != 0 or len(matchsticks) < 4:
            return False
        side=total // 4
        sticks=sorted(matchsticks,reverse=True)
        if sticks[0] > side:
            return False
        sides=[0]*4
        def dfs(i):
            if i == len(sticks):
                return True
            seen=set()
            for k in range(4):
                if sides[k] + sticks[i] > side or sides[k] in seen:
                    continue
                seen.add(sides[k])
                sides[k] += sticks[i]
                if dfs(i+1):
                    return True
                sides[k] -= sticks[i]
            return False
        return dfs(0)