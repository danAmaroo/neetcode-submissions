class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or len(token) > 1 and token[0] == "-":
                stack.append(int(token))
            else:
                num1 = stack.pop() # 2
                num2 = stack.pop() # 1
                ans = 0
                if token == "+":
                    ans = num1 + num2
                elif token == "-":
                    ans = num2 - num1
                elif token == "*":
                    ans = num1 * num2
                elif token == "/":
                    ans = int(num2 / num1)
                stack.append(ans)
        
        return int(stack[0])
                

