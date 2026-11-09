class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) ->  bool:
            days_needed = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += w
            return days_needed <= days
        low=max(weights)
        high=sum(weights)
        while low < high:
            mid=(low+high) // 2
            if can_ship(mid):
                high = mid
            else:
                low = mid+1
        return low