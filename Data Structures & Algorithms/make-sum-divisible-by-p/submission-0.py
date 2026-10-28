class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0:
            return 0

        n = len(nums)
        last={0: -1}
        prefix = 0
        best = n

        for j,x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - r) % p
            if need in last:
                best = min(best, j - last[need])
            last[prefix] = j
        return best if best < n else -1