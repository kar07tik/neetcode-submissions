class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(open_count: int,close_count: int,path: list[str]):
            if open_count == close_count == n:
                res.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1,close_count,path)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(open_count,close_count + 1,path)
                path.pop()
        backtrack(0,0,[])
        return res
        