class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #if not stack, add num
        #set pointer to start of res
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([temp, i])
        return res