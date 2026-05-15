class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        #.          i
        #stack [28,40,35]
        # [2,1,0,0]
        #init res
        res = []
        stack = []
        #iterate in reverse
        for i in range(len(temperatures)-1,-1,-1):
            #if empty stack insert 0 at start of res
            if len(stack) == 0:
                res.insert(0,0)
            # else
            else:
                days = 0
                #iterate stack
                for j in range(len(stack)-1,-1,-1):
                    #count how many many are more than current temp
                    if temperatures[stack[j]] > temperatures[i]:
                        days = stack[j] - i
                        break
                res.insert(0,days)
            
            # add temp to stack
            stack.append(i)
        return res

