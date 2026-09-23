class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Virtual 1D binary search over range [0, ROWS * COLS - 1]
        low, high = 0, ROWS * COLS - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map 1D index back to 2D matrix coordinates
            row = mid // COLS
            col = mid % COLS
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False