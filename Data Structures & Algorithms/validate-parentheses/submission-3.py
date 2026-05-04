class Solution:
    def isValid(self, s: str) -> bool:
        parenthesissets = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in parenthesissets:
                if stack and stack[-1] == parenthesissets[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False 


        