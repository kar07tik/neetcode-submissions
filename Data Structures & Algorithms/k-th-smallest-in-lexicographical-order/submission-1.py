class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count(prefix):
            curr = prefix
            nxt = prefix + 1
            steps = 0

            while curr <= n:
                steps += min(n + 1, nxt) - curr
                curr *= 10
                nxt *= 10

            return steps

        curr = 1
        k -= 1

        while k > 0:
            steps = count(curr)

            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr