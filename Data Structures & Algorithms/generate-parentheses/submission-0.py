class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open < n
        #only add close paranthesis if closed < open
        #valid if open == closed == n
        stack = []
        res = []

        def backtrack(openNum, closedNum):
            if openNum == closedNum == n:
                res.append(''.join(stack))
                return
            
            if openNum < n:
                stack.append('(')
                backtrack(openNum + 1, closedNum)
                stack.pop()
            
            if closedNum < openNum:
                stack.append(')')
                backtrack(openNum, closedNum + 1)
                stack.pop()
        backtrack(0, 0)
        return res