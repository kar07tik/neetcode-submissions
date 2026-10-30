from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0,0]
        for s in students:
            count[s] += 1
        remaining = len(students)
        for sw in sandwiches:
            if count[sw] == 0:
                break
            count[sw] -= 1
            remaining -= 1
        return remaining