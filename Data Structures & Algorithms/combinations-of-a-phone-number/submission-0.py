class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result=[]
        def backtrack(index,current_string):
            if index == len(digits):
                result.append(current_string)
                return
            current_digit=digits[index]
            for char in digit_to_char[current_digit]:
                backtrack(index+1,current_string+char)
        backtrack(0,"")
        return result
        