class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(first) + int(second)))
            elif c == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(first) - int(second)))
            elif c == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(first) * int(second)))
            elif c == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(str(int(int(first) / int(second))))
            else:
                stack.append(c)
        return int(stack[-1])

        