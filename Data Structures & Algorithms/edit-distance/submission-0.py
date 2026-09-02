class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a 2D DP array of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: 
        # If word2 is empty, we must delete all characters from word1
        for i in range(m + 1):
            dp[i][0] = i
            
        # If word1 is empty, we must insert all characters of word2
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Minimum of Insert, Delete, or Replace + 1 operation
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],    # Insert
                        dp[i - 1][j],    # Delete
                        dp[i - 1][j - 1] # Replace
                    )
                    
        return dp[m][n]