#Brainstorm
# gas = [1,2,3,4],  
#cost = [2,2,4,1]
#diff = [-1,0,-1,3]
#              x
# total = 0                               
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the sum of gas < sum cost return -1
        #because that means there isnt going to be enough gas to cover the trip
        if sum(gas) < sum(cost):
            return -1
        
        #
        total = 0 
        #starting pos
        res = 0
        #for each element in the gas array
        for i in range(len(gas)):
            # the total += the amount of gas at that spot minus the cost
            total += (gas[i] - cost[i])
            #if the total is negative that means cost is more than gas
            #so it cant start from here
            #reset total and move to the next starting spot
            #in the list
            if total < 0:
                total = 0
                res = i + 1
        #return the result index that works
        return res