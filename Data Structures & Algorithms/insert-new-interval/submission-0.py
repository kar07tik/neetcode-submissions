class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # If the new interval is completely before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # Since the rest are non-overlapping, we can just append all remaining intervals
                return res + intervals[i:]
            
            # If the new interval is completely after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # If the intervals overlap, merge them into the newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                
        # If we iterate through all intervals without returning, append the merged newInterval
        res.append(newInterval)
        
        return res