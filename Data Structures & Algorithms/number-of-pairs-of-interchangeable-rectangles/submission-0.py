from math import gcd
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        seen=defaultdict(int)
        pairs=0

        for w,h in rectangles:
            g=gcd(w,h)
            key=(w//g,h//g)
            pairs += seen[key]
            seen[key] += 1
        return pairs
