class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)

        def shift_down(root: int, end: int) -> None:
            while True:
                child = 2 * root + 1
                if child >= end:
                    break
                if child + 1 < end and nums[child + 1] > nums[child]:
                    child += 1
                if nums[root] >= nums[child]:
                    break
                nums[root], nums[child] = nums[child],nums[root]
                root = child 
        
        for i in range(n // 2 - 1, -1, -1):
            shift_down(i,n)

        for end in range(n - 1,0,-1):
            nums[0],nums[end]= nums[end],nums[0]
            shift_down(0,end)
        return nums