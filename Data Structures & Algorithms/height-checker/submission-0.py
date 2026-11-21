class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        mismatches=0
        for h, exp in zip(heights,expected):
            if h != exp:
                mismatches += 1
        return mismatches