class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [1,2,1,0,0]
        #init list with 0's
        res = [0] * len(temperatures)
        #iterate right to left
        for i in range(len(temperatures)-1,-1,-1):
            # if seen is empty res is 0 
            if (i == len(temperatures)-1):
                pass
            else:
                #if its not iterate left to right
                #until you hit bigger num
                for j in range(i, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        res[i] = j-i
                        break
        return res

        
