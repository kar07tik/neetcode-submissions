class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        memo={}

        def dp(r1,c1,r2):
            c2=r1+c1-r2

            if (r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            if r1 == n - 1 and c1 == n - 1:
                return grid[n - 1][n - 1]
            if (r1,c1,r2) in memo:
                return memo[(r1,c1,r2)]
            if r1 == r2 and c1 == c2:
                ans = grid[r1][c1]
            else:
                ans = grid[r1][c1] + grid[r2][c2]
            
            ans += max(
                dp(r1,c1+1,r2),
                dp(r1,c1+1,r2+1),
                dp(r1+1,c1,r2),
                dp(r1+1,c1,r2+1)
            )
            memo[(r1,c1,r2)] = ans
            return ans
        res = dp(0,0,0)
        return max(0,res)
        