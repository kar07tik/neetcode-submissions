class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=min(len(word1),len(word2))
        merged= ''.join(a+b for a,b in zip(word1,word2))
        return merged+word1[k:]+word2[k:]