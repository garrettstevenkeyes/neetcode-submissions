#Brainstorm
# gas = [1,2,3,4],  
#cost = [2,2,4,1]
#diff = [-1,0,-1,3]
#              x
# total = 0                               
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the sum of gas < sum cost return -1
        if sum(gas) < sum(cost):
            return -1
        
        total = 0 
        #starting pos
        res = 0
        for i in range(len(gas)):
            # 
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res