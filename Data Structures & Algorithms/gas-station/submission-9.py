class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #init res
        res = 0
        #if the sum of the gas is less than the cost you return -1
        if sum(gas) < sum(cost):
            return -1
        #iterate the list from first index
        idx = 0
        total = 0
        while idx < len(gas):
            #add to the total gas minus cost
            total += (gas[idx] - cost[idx])
            #if the total is below 0 that space doesnt work
            if total < 0:
                #reset total 
                total = 0
                #move the result
                res = idx + 1
            #interate 
            idx += 1
        return res
