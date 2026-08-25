class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # stack = (, [, {

        if len(s) < 2:
            return False

        for letter in s:
            if letter == '(' or letter == '{' or letter == '[':
                stack.append(letter)
                next 
            elif len(stack) == 0:
                return False
            elif letter == ')' and stack[len(stack) - 1] == '(':
                stack.pop()
            elif letter == '}' and stack[len(stack) - 1] == '{':
                stack.pop()
            elif letter == ']' and stack[len(stack) - 1] == '[':
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        
        return False




