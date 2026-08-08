class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


# Input
low = 2
high = 9

# Create object
obj = Solution()

# Call function
result = obj.countOdds(low, high)

# Output
print(result)