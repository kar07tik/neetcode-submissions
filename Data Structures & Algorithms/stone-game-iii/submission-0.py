from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp1=dp2=dp3=0
        for i in range(n-1,-1,-1):
            best=float("-inf")
            stones_taken=0
            for k in range(1,4):
                if i + k - 1 >= n:
                    break
                stones_taken += stoneValue[i + k -1]
                next_dp = dp1 if k == 1 else (dp2 if k == 2 else dp3)
                best = max(best,stones_taken - next_dp)
            dp3,dp2,dp1=dp2,dp1,best
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"