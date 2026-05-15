class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #define left and right pointers
        #our max pile size is the max per hour
        #so left is 0 and right is that max
        left, right = 1, max(piles)
        #we want the minimum so we can init it to the max possible
        #which is our right
        res = right
        while left <= right:
            #find mid point
            k = (left + right) // 2
            #for our rate, how many hours does it take to 
            #eat all the bananas
            hours = 0
            for p in piles:
                #divide our pile by our mid point rate
                #use math.ceil to round up because you
                #can use fractional time and need to eat the 
                #whole pile
                hours += math.ceil(p/k)
            #if our hours spent eating is less than h
            if hours <= h:
                #take the minimum
                #of our midpoint value
                res = min(res, k)
                #move left
                right = k - 1
            else:
                #move right
                left = k + 1
        return res

