class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        in1=[False]*1001
        for x in nums1:
            in1[x]=True
        res=[]
        for x in nums2:
            if in1[x]:
                res.append(x)
                in1[x]=False
        return res