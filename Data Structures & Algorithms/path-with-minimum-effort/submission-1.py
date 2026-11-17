class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R,C =len(heights),len(heights[0])
        pq=[(0,0,0)]
        dist={(0,0): 0}
        while pq:
            d,r,c = heapq.heappop(pq)
            if (r,c) == (R-1, C-1): return d
            if d > dist.get((r,c), float('inf')): continue

            for nr,nc in ((r-1,c), (r+1,c),(r,c-1),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if nd < dist.get((nr,nc), float('inf')):
                        dist[(nr,nc)] = nd
                        heapq.heappush(pq,(nd,nr,nc))