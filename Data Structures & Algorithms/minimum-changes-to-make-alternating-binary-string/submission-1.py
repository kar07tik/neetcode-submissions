class Solution:
    def minOperations(self, s: str) -> int:
        mismatches_start_with_zero=0
        for i, ch in enumerate(s):
            expected = "0" if i % 2 == 0 else "1"
            if ch != expected:
                mismatches_start_with_zero += 1
        return min(mismatches_start_with_zero, len(s) - mismatches_start_with_zero)