class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}  # Correct mapping
        stack = []

        for char in s:
            if char in mapping.values():  # opening brackets
                stack.append(char)
            elif char in mapping.keys():  # closing brackets
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return not stack