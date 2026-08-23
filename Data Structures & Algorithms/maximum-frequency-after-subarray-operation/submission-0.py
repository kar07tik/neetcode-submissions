class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base_k_count = nums.count(k)
        max_increase = 0
        
        unique_nums = set(nums)
        
        for v in unique_nums:
            if v == k:
                continue
            
            curr_increase = 0
            max_curr_increase = 0

            for num in nums:
                if num == v:
                    curr_increase += 1
                elif num == k:
                    curr_increase -= 1

                if curr_increase < 0:
                    curr_increase = 0
                
                if curr_increase > max_curr_increase:
                    max_curr_increase = curr_increase

            if max_curr_increase > max_increase:
                max_increase = max_curr_increase

        return base_k_count + max_increase