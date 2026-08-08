from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # If they don't have the same repeating pattern,
        # no common divisor string exists.
        if str1 + str2 != str2 + str1:
            return ""
        
        # Length of the largest common divisor string
        length = gcd(len(str1), len(str2))
        
        return str1[:length]