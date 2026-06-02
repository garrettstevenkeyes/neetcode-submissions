class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #max has to be the largest pile size
        start, end = 1, max(piles)
        minBananaRate = max(piles) 
        while start <= end:
            hoursTaken = 0
            midBananaRate = (start + end) // 2
            for num in piles:
                hoursTaken += math.ceil(num/midBananaRate)
            
            if hoursTaken <= h:
                end = midBananaRate - 1
                minBananaRate = min(minBananaRate, midBananaRate)
            else:
                start = midBananaRate + 1
            
        
        return minBananaRate

