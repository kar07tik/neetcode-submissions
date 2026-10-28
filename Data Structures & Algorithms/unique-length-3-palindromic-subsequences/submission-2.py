class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=0
        for c in set(s):
            first=s.find(c)
            last=s.rfind(c)
            if last - first > 1:
                res += len(set(s[first + 1:last]))
        return res
    