class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in closeToOpen:
                # If it's a closing bracket, check for a matching top of stack
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # Return True only if all brackets were properly matched and popped
        return len(stack) == 0