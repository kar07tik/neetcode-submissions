class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={c: i for i,c in enumerate(order)}
        keys=[[rank[c] for c in w] for w in words]
        return keys == sorted(keys)