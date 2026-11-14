from functools import lru_cache
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words=set(wordDict)
        max_len=max(len(w) for w in wordDict)
        n=len(s)

        @lru_cache(None)
        def sentences(i):
            if i == n:
                return [""]
            res=[]
            for j in range(i + 1, min(n,i + max_len) + 1):
                word=s[i:j]
                if word in words:
                    for rest in sentences(j):
                        res.append(word + (" " + rest if rest else ""))
            return res
        return sentences(0)