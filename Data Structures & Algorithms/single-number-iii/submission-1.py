class Solution:
    def singleNumber(self, nums):
        xor = 0
        for x in nums:
            xor ^= x

        diff = xor & -xor

        a = b = 0
        for x in nums:
            if x & diff:
                a ^= x
            else:
                b ^= x

        return [a, b]