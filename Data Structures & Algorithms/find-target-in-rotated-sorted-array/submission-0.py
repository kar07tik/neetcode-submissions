class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target is in the left half
                else:
                    l = mid + 1  # Target is in the right half
            # Otherwise, right half must be sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target is in the right half
                else:
                    r = mid - 1  # Target is in the left half

        return -1