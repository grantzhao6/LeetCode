class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in \+-*/\:
                a2 = stack.pop()
                a1 = stack.pop()
                if x == '+':
                    stack.append(a1+a2)
                elif x == '-':
                    stack.append(a1-a2)
                elif x == '*':
                    stack.append(a1*a2)
                elif x == '/':
                    stack.append(int(a1/a2))
            else:
                stack.append(int(x))
        return stack.pop()
