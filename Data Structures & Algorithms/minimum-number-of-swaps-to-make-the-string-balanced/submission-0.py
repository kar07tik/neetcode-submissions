class Solution:
    def minSwaps(self, s: str) -> int:
        open_count=0
        unmatched=0

        for ch in s:
            if ch == '[':
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                unmatched += 1
        return (unmatched + 1) // 2