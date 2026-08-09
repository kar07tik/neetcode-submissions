from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        
        for num in nums:
            # Find the index of the first element >= num
            idx = bisect_left(tails, num)
            
            # If num is greater than all elements in tails, append it
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise, overwrite the existing element to keep values as small as possible
                tails[idx] = num
                
        return len(tails)