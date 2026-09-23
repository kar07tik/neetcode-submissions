import math
from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            # Calculate total hours needed to eat all bananas at speed k
            total_time = sum(math.ceil(p / k) for p in piles)

            if total_time <= h:
                res = k
                r = k - 1  # Try searching for a smaller speed
            else:
                l = k + 1  # Speed is too slow, increase lower bound

        return res