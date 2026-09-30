class Solution:
    def isValid(self, s: str) -> bool:
        clopen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for char in s:
            if char not in clopen:
                stack.append(char)
            else:
                if stack and stack[-1] == clopen[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack
        