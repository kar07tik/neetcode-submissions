class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: Move stones to the right due to gravity after rotation
        for row in boxGrid:
            empty = n - 1

            for j in range(n - 1, -1, -1):

                if row[j] == '*':
                    empty = j - 1

                elif row[j] == '#':
                    row[j] = '.'
                    row[empty] = '#'
                    empty -= 1

        # Step 2: Rotate the box 90 degrees clockwise
        result = [['.'] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]

        return result