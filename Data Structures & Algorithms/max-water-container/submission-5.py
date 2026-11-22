class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights)-1
        res = 0
        while start < end:
            volume = min(heights[start], heights[end]) * (end-start)
            res = max(res, volume)

            if heights[end] > heights[start]:
                start += 1
            else:
                 end -= 1
        
        return res