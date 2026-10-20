from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        queue=deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            row,col=queue.popleft()
            for dr,dc in directions:
                next_row,next_col = row + dr, col + dc
                if (
                    0 <= next_row < rows 
                    and 0 <= next_col < cols 
                    and grid[next_row][next_col] == 2147483647
                ):
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row,next_col))
if __name__ == "__main__":
    examples = [
        [
            [2147483647, -1,0,2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1,2147483647, -1],
            [0, -1 , 2147483647,2147483647],
        ],
        [[0,-1],[2147483647,2147483647]],
    ]
    
    solution = Solution()
    for grid in examples:
        solution.islandsAndTreasure(grid)
        print(grid)


