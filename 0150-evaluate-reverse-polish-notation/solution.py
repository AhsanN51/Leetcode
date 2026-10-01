class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = stack.pop()   # right operand
                a = stack.pop()   # left operand
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    stack.append(q if (a < 0) == (b < 0) else -q)
        return stack[-1]
