class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        total=n*n
        freq=[0]*(total+1)
        for row in grid:
            for val in row:
                freq[val] += 1
        repeated = missing = -1
        for num in range(1,total+1):
            if freq[num]==2:
                repeated=num
            elif freq[num] == 0:
                missing = num
        return [repeated,missing]