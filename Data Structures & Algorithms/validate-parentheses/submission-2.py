class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen: dict[str, str] = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack: list[str] = []

        for char in s:
            if char not in closeOpen:
                stack.append(char)
            elif stack and stack[-1] == closeOpen[char]:
                stack.pop()
            else:
                return False
            
        return not stack
        