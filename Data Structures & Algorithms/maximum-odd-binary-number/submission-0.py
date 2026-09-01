class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count('1')
        zeros_count = s.count('0')
        return '1' * (ones_count -1) + '0' * zeros_count + '1'
        