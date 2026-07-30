from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point):
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point):
        x, y = point
        ans = 0

        for (px, py), freq in list(self.points.items()):

            if px != x and abs(px - x) == abs(py - y):
                ans += (
                    freq
                    * self.points[(x, py)]
                    * self.points[(px, y)]
                )

        return ans