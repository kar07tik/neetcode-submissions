from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(n + 1):
            count = 0
            for v in nums:
                if v >= x:
                    count += 1
            if count == x:
                return x
        return -1