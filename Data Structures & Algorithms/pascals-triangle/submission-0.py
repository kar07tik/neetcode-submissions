class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows - 1):
            # Create a temporary array with 0s on both ends
            temp = [0] + res[-1] + [0]
            row = []
            
            # Build the new row by summing adjacent elements
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
                
            res.append(row)
            
        return res