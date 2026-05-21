class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '[':']', '{':'}'}
        stack = []

        for i in s:
            if i in d:
                stack.append(i)
            elif stack == [] or d[stack.pop()] != i:
                return False

        return stack == []