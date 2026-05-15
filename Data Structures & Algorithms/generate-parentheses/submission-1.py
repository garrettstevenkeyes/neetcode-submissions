class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #init a stack and res
        stack = []
        res = []

        #def dfs takes and closed count
        def dfs(openCount, closedCount, stack):
            # if open count == closed == n
            if openCount == closedCount == n:
                #add to the result
                res.append(''.join(stack)) 
                #return
                return 

            # if open count if less than n
            if openCount < n:
                #add open to the stack
                stack.append('(')
                # recurse
                dfs(openCount + 1, closedCount, stack)
                #remove
                stack.pop()

            # if closed count if less than open count
            if closedCount < openCount:
                #add close to the stack
                stack.append(')')
                # recurse
                dfs(openCount, closedCount + 1, stack)
                #remove
                stack.pop()
        
        dfs(0,0,[])
        return res