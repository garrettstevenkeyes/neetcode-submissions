#we are looking for the min int, this means its likely a binary search 
#type problem
#binary search has log n time complexity 
# O(1) space complexity
#binary search on the solution space

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #init left, right, res
        left, right = 1, max(piles)
        #set rate to the right
        bananaRate = right
        #iterate
        while left <= right:
            testRate = (left + right) // 2
            #iterate banana piles
            curRateSum = 0
            #check all the piles
            for pile in piles:
                #check how long it takes to eat a pile
                curRateSum += math.ceil(pile / testRate)
            #after checking all piles
            if curRateSum <= h:
                bananaRate = min(bananaRate, testRate)
                #if less than or equal move left
                right = testRate - 1
            else:
                #if greater than h move right
                left = testRate + 1
            
        return bananaRate
            

