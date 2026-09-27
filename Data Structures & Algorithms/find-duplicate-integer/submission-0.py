class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        
        # Step 1: Find the intersection point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Step 2: Find the entrance to the cycle (duplicate element)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow