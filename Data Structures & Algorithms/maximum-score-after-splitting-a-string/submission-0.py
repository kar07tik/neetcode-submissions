class Solution:
    def maxScore(self, s: str) -> int:
        total_ones=s.count("1")
        zeros=0
        ones_left=0
        max_score=0
        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones_left += 1
            ones_right = total_ones - ones_left
            score = zeros + ones_right
            if score > max_score:
                max_score=score
        return max_score