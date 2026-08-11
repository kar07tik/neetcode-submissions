class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start times
        intervals.sort(key=lambda i: i[0])
        
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            
            # Check if current interval overlaps with the previous one
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
                
        return merged