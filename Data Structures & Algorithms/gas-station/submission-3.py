# g = [1,2,3,4]
# c = [2,2,4,1]
#      i
#general idea is if the cost is more than the gas 
#we cant do that travel

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #if sum of gas less than sum cost
        if sum(gas) < sum(cost):
            return -1

        #current total
        total = 0
        #res idx
        res = 0
        #iterate over gas list
        for i in range(len(gas)):
            # add to total gas minus cost
            total += (gas[i] - cost[i])
            #if the total is less than 0 it wont work
            if total < 0:
                #reset total
                total = 0
                #iterate res
                res = i + 1
        #return res
        return res