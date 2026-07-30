class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]

            heights = sorted(matrix[i], reverse=True)

            for j in range(n):
                area = heights[j] * (j + 1)
                ans = max(ans, area)

        return ans