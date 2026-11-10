class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit: int) -> bool:
            parts=1
            current=0
            for x in nums:
                if current + x > limit:
                    parts += 1
                    current = 0
                current += x
            return parts <= k
        low=max(nums)
        high=sum(nums)
        while low < high:
            mid=(low+high) // 2
            if can_split(mid):
                high=mid
            else:
                low=mid+1
        return low