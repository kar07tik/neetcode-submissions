class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, target: int, current: list[int]):
            if target == 0:
                res.append(list(current))
                return

            for i in range(start, len(candidates)):
                # Skip duplicate elements at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Stop exploring if the candidate exceeds the remaining target
                if candidates[i] > target:
                    break

                current.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current)
                current.pop()

        backtrack(0, target, [])
        return res