#Brainstorm
# Time O(N)
# Space O(1)

#Plan
# 1. create two pointers on each end of the container
# 1.5 get max value
# 2. Compare the heights of the pillars, whichever is smaller move in
#  because we want to look for max height
#2.5 get max value again
# 3. do this until the pointers are equal and return the max

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. create two pointers on each end of the container
        start,end = 0, len(heights)-1
        # 1.5 get max value
        maxVol = 0
        
        while start < end:
            # 2. Compare the heights of the pillars, whichever is smaller move in
            #  because we want to look for max height
            volume = min(heights[start], heights[end]) * (end - start)
            maxVol = max(maxVol, volume)

            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        
        return maxVol