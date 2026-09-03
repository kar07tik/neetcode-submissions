class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix),len(matrix[0])
        dp={}
        def dfs(r: int, c: int) -> int:
            if(r,c) in dp:
                return dp[(r,c)]
            res = 1
            for dr , dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr , nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr,nc))
            dp[(r,c)] = res
            return res 

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
        return max(dp.values())
        