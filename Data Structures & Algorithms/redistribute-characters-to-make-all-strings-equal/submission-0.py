class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        counts=Counter("".join(words))
        return all(freq % n == 0 for freq in counts.values())