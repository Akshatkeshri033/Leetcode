# Last updated: 8/20/2025, 5:50:00 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # if it's an opening bracket
                stack.append(char)
            elif char in mapping:  # if it's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
