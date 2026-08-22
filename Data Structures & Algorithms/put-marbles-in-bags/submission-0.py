class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
 
        if k == 1 or k == len(weights):
            return 0

        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])
            

        pair_sums.sort()
        

        min_score_splits = sum(pair_sums[:k - 1])
        max_score_splits = sum(pair_sums[-(k - 1):])
        
        return max_score_splits - min_score_splits