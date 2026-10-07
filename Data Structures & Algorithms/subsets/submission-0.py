class Solution:
    def subsets(self, nums):
        ans = []

        def backtrack(index, current):
            ans.append(current.copy())

            for i in range(index, len(nums)):
                current.append(nums[i])

                backtrack(i + 1, current)

                current.pop()

        backtrack(0, [])

        return ans