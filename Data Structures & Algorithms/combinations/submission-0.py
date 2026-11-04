class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]

        def backtrack(start):
            if len(path) == k:
                ans.append(path[:])
                return 

            need = k - len(path)
            for num in range(start,n - need + 2):
                path.append(num)
                backtrack(num+1)
                path.pop()

        backtrack(1)
        return ans 