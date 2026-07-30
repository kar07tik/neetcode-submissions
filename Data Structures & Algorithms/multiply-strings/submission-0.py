class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                p1 = i + j
                p2 = i + j + 1

                total = product + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        # Remove leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str