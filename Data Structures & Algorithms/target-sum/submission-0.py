class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)

        # Let P be the subset of numbers with a positive sign, and N be the negative subset.
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) = total_sum
        # Adding both: 2 * sum(P) = target + total_sum  =>  sum(P) = (target + total_sum) / 2
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0

        subset_sum = (total_sum + target) // 2

        # 1D dynamic programming for 0/1 Knapsack (Subset Sum)
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # 1 way to get sum 0 (choose empty subset)

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]