class Solution:
    #time O(N)
    #space (1)
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxWater = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            maxWater = max(maxWater, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater