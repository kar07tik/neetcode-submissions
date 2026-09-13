class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        if m + n != len(s3):
            return False
        
        # Ensure s2 is the shorter string for O(min(m, n)) space
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m
            
        # dp[j] indicates if s1[:i] and s2[:j] can interleave to form s3[:i + j]
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Base case for matching s2 against s3 prefix
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = from_s1 or from_s2
                
        return dp[n]