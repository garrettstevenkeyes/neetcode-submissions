#Brainstorm
#maintain two stacks, one is seen items, one is min 
#for each item we add add to the main stack and compare with the 
#end of the min stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []        

    def push(self, val: int) -> None:
        #compare with min stack
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

        #add to main stack
        self.stack.append(val)
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
