class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '(' or c in '[' or c in '{':
                stack.append(c)
            else:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0