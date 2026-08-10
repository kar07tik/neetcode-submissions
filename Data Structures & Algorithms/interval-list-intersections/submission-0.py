class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            # Calculate the potential intersection boundaries
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If a valid intersection exists, add it to the result
            if start <= end:
                res.append([start, end])

            # Move the pointer pointing to the interval that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res