class Solution:
    def myPow(self, x: float, n: int) -> float:

        # If n is negative:
        # x^(-n) = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n > 0:

            # If n is odd
            if n % 2 == 1:
                ans = ans * x

            # Square x
            x = x * x

            # Divide n by 2
            n = n // 2

        return ans