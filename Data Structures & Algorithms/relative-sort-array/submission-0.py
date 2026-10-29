class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank={v: i for i,v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (rank.get(x, len(arr2)),x))