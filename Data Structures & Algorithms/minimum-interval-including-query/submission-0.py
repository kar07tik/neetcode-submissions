import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        # Keep track of original query indices to return results in order
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        min_heap = []  # Stores tuples of (interval_length, right_end)
        i = 0
        n = len(intervals)
        
        for q, orig_idx in sorted_queries:
            # Add all intervals that start before or at query point `q`
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(min_heap, (length, right))
                i += 1
            
            # Remove intervals from the heap that end before query point `q`
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # The top of the min-heap is the smallest valid interval containing `q`
            if min_heap:
                res[orig_idx] = min_heap[0][0]
                
        return res