class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(':')' , '[':']', '{':'}'}
        stack = []
        for char in s:
            if char in pars.values():
                if not stack or stack.pop() != char:
                    return False
            else:
                stack.append(pars[char])
        return not stack