class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # dp1 represents ways to decode s[i+1:]
        # dp2 represents ways to decode s[i+2:]
        dp1 = 1  # Base case for empty suffix
        dp2 = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                current = 0
            else:
                current = dp1
                # Check if two-digit decoding (10-26) is valid
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                    current += dp2
            
            # Shift state variables
            dp2 = dp1
            dp1 = current
            
        return dp1