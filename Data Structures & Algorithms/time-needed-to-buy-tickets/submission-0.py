from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        need = tickets[k]
        total=0
        for i,t in enumerate(tickets):
            if i <= k:
                total += min(t,need)
            else:
                total += min(t, need - 1)
        return total