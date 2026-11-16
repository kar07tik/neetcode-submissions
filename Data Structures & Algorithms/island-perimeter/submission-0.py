class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land=pairs=0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    land += 1
                    pairs += (i > 0 and grid[i - 1][j] == 1) + (j > 0 and row[j - 1] == 1)
        return 4 * land - 2 * pairs