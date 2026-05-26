class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = [0]
        #prev = 0
        # res = [1,0,0,0,0,0,0]
        #init list with 0's
        res = [0] * len(temperatures)

        stack = []
        #iterate right to left
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()

                res[prev_i] = i - prev_i
            stack.append(i)
        return res

        
