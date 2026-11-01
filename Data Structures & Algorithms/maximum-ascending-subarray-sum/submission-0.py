from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                cur=nums[i]
            best=max(best,cur)
        return best