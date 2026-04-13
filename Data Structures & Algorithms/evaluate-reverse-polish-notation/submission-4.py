class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stack = []
        for c in tokens:
            if c in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[c](a, b))
            else:
                stack.append(int(c))
        return stack[-1]