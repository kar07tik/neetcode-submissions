from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=c2=None
        n1=n2=0

        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
            elif n1 == 0:
                c1,n1 = x,1
            elif n2 == 0:
                c2,n2 = x,1
            else:
                n1 -= 1
                n2 -= 1
        limit = len(nums) // 3
        res=[]
        if c1 is not None and nums.count(c1) > limit:
            res.append(c1)
        if c2 is not None and nums.count(c2) > limit:
            res.append(c2)
        return res
