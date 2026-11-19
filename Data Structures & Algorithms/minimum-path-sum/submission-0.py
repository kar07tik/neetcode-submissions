from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[0]*cols
        dp[-1]=grid[-1][-1]
        for c in range(cols - 2, -1, -1):
            dp[c] = grid[-1][c] + dp[c+1]
        for r in range(rows - 2, -1, -1):
            dp[-1] += grid[r][-1]
            for c in range(cols - 2, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c+1])
        return dp[0]