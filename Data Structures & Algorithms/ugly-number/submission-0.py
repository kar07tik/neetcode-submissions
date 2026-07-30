class Solution:
    def isUgly(self, n: int) -> bool:

        # 0 and negative numbers are not ugly
        if n <= 0:
            return False

        # Remove all factors of 2
        while n % 2 == 0:
            n //= 2

        # Remove all factors of 3
        while n % 3 == 0:
            n //= 3

        # Remove all factors of 5
        while n % 5 == 0:
            n //= 5

        # If nothing other than 2, 3, 5 was a factor,
        # n will become 1
        return n == 1