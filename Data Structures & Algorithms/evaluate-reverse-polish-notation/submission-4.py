class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        #
        # ["1","2","+","3","*","4","-"] 
        #                           i
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                second = stack.pop()
                stack.append(stack.pop() - second)
            elif char == '/':
                second = stack.pop()
                stack.append(int(stack.pop() / second))
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(char))
        return stack[0]