class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on their start times
        intervals.sort(key=lambda x: x[0])

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # Non-overlapping condition
            if start >= prevEnd:
                prevEnd = end
            else:
                # Overlapping condition: increment remove count
                res += 1
                # Greedily keep the interval that ends earlier to minimize future overlaps
                prevEnd = min(prevEnd, end)

        return res