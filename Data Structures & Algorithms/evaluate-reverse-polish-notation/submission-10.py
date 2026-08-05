class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])        
        for token in tokens:
            if token == "+":
                sum = int(stack.pop()) + int(stack.pop())
                stack.append(sum)
            elif token == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                sum = int((b - a))
                stack.append(sum)
            elif token == "*":
                sum = int(stack.pop()) * int(stack.pop())
                stack.append(sum)
            elif token == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                sum = int((b / a))
                stack.append(sum)
            else:
                stack.append(token)

        return stack[0]