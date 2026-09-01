class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        
        is_possible = False
        for i in range(1, n // 2 + 1):
            if (total_sum * i) % n == 0:
                is_possible = True
                break
                
        if not is_possible:
            return False
        
        dp = [0] * (n // 2 + 1)
        dp[0] = 1  
        
        for num in nums:
            
            for i in range(n // 2, 0, -1):
                
                dp[i] |= (dp[i - 1] << num)
                
        for i in range(1, n // 2 + 1):
            if (total_sum * i) % n == 0:
                target_sum = (total_sum * i) // n
                
                if dp[i] & (1 << target_sum):
                    return True
                    
        return False