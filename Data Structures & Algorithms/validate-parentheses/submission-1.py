class Solution:
    def isValid(self, s: str) -> bool:
        closetobegin = {']':'[', '}':'{', ')':'('}
        stack = []
        for i in s:
            if i in closetobegin:
                if stack and stack[-1] == closetobegin[i]:
                    stack.pop();
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        