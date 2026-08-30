class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        max_y_for_x = {}

        for xi, yi in zip(x,y):
            if xi not in max_y_for_x or yi > max_y_for_x[xi]:
                max_y_for_x[xi] = yi
        
        if len(max_y_for_x) < 3:
            return -1
        
        top_3_y = heapq.nlargest(3,max_y_for_x.values())
        return sum(top_3_y)
        