class MinStack:
    stack = [[]]

    def __init__(self):
        self.stack = [[]]

    def push(self, val: int) -> None:
        old_min = self.stack.pop()
        self.stack.append(old_min)
        if len(self.stack) == 1:
            min_num = val
        else:
            min_num = min(val, old_min[1])
        self.stack.append([val, min_num])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]
        

        
