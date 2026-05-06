class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(first + second))
            elif t == '-':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(first - second))
            elif t == '*':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(first * second))
            elif t == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(str(int(first / second)))
            else:
                stack.append(t)

        return (int(stack.pop()))
