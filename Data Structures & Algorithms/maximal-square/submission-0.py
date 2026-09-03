class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        ROWS , COLS = len(matrix) , len(matrix[0])
        dp=[0] *(COLS + 1)
        max_side = 0
        prev = 0
        for r in range(ROWS):
            for c in range(COLS):
                temp = dp[c + 1]
                if matrix[r][c] == "1":
                    dp[c + 1] = 1 + min(dp[c],dp[c + 1],prev)
                    max_side = max(max_side,dp[c + 1])
                else:
                    dp[c + 1] = 0
                prev = temp
        return max_side * max_side

        