class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are never palindromes
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:

            # Get last digit
            digit = x % 10

            # Add digit to reverse
            reverse = reverse * 10 + digit

            # Remove last digit from x
            x //= 10

        return original == reverse