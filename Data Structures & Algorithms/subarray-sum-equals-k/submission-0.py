class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count={0: 1}
        s=0
        ans=0
        for x in nums:
            s += x
            ans += count.get(s-k,0)
            count[s] = count.get(s,0)+1
        return ans