class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff=[0] * 1002 
        for p, start,end in trips:
            diff[start] += p
            diff[end] -= p
        current=0
        for change in diff:
            current += change
            if current > capacity:
                return False
        return True