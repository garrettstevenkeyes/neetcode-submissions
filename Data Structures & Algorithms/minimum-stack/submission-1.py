class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #add to the stack
        self.stack.append(val)
        #if the minStack is empty
        if len(self.minStack) == 0:
            self.minStack.append(val)
        #if the value is less than the top add it to min
        #otherwise add the min
        else:
            if self.minStack[-1] < val:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)
        

    def pop(self) -> None:
        #remove top of min stack
        self.minStack.pop()
        #return top of stack
        return self.stack.pop()

    def top(self) -> int:
        #return the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        #return the min stack item
        return self.minStack[-1]
