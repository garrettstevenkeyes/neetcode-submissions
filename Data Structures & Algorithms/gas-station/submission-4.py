# 
#  gas =  [1,2,3,4]
#  cost = [2,2,4,1]
#.         i
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        #if the sum of gas < sum cost, never enough gas
        if sum(gas) < sum(cost):
            return -1
        #init total
        total = 0
        #iterate the two in while loop
        i = 0
        while i < len(gas):
            # add to the total
            total += (gas[i] - cost[i])
            # if the total is less than 0
            if total < 0:
                total = 0
                res = i + 1
            
            i += 1
        return res

