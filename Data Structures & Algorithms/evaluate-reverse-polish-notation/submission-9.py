class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opr = {'+':lambda a,b : a+b, 
        '-':lambda a,b : a-b,
        '*':lambda a,b : a*b,
        '/':lambda a,b : int(a/b)}
        for t in tokens:
            if t in opr:
                b,a = stack.pop(), stack.pop()
                stack.append(opr[t] (a,b))
            else:
                stack.append(int(t))
        return stack[-1]
            
