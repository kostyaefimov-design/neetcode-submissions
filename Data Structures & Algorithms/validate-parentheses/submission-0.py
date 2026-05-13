class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in range(len(s)):
            if not queue:
                queue.append(s[i]) 
            else:
                if s[i] == "(" or s[i] == "[" or s[i] == "{":
                    queue.append(s[i])
                if s[i] == ")" and queue[-1] != "(":
                    return False
                elif s[i] == ")" and queue[-1] == "(":
                    del queue[-1]
                if s[i] == "]" and queue[-1] != "[":
                    return False
                elif s[i] == "]" and queue[-1] == "[":
                    del queue[-1]
                if s[i] == "}" and queue[-1] != "{":
                    return False
                elif s[i] == "}" and queue[-1] == "{":
                    del queue[-1]
        return not queue    