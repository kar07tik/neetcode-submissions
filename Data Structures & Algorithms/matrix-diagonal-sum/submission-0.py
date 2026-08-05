from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0

        for i in range(n):
            ans += mat[i][i]  # Primary diagonal

            if i != n - 1 - i:   # Avoid double-counting center
                ans += mat[i][n - 1 - i]

        return ans