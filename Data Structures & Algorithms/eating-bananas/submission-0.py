class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        l, r = 1, max(piles)
        while l < r:
            midHours = l + ((r - l)//2)
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/midHours)
            
            if total_hours > h:
                l = midHours+1
            else:
                r = midHours
        return l
            
            