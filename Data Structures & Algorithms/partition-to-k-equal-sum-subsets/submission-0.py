class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total % k:
            return False
        target = total // k
        nums = sorted(nums, reverse=True)
        if nums[0] > target:
            return False
        buckets=[0] * k

        def dfs(i):
            if i == len(nums):
                return True
            seen=set()
            for j in range(k):
                if buckets[j] + nums[i] > target or buckets[j] in seen:
                    continue
                seen.add(buckets[j])
                buckets[j] += nums[i]
                if dfs(i+1):
                    return True
                buckets[j] -= nums[i]
            return False
        return dfs(0)