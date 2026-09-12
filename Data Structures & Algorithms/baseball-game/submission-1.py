class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if op.isdigit() or op[0] == "-":
                stack.append(op)
            elif op == "+":
                prev = stack.pop()
                tmp = stack.pop()
                stack.append(tmp)
                stack.append(prev)
                stack.append(int(tmp) + int(prev))
            elif op == "D":
                tmp = stack.pop()
                stack.append(tmp)
                stack.append(int(tmp) * 2)
            elif op == "C":
                stack.pop()
        
        ans = 0
        for num in stack:
            ans += int(num)

        return ans


