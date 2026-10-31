
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        u=sum(set(nums))
        return [sum(nums) - u, n * (n+1) // 2 - u]        