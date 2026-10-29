class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free_at = 0
        total_wait = 0

        for arrival, prep in customers:
            start = max(free_at, arrival)
            free_at = start + prep
            total_wait += free_at - arrival
        
        return total_wait / len(customers)