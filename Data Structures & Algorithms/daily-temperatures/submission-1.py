class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # stores pairs: [temp, index] or simply index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append([temp, i])

        return res