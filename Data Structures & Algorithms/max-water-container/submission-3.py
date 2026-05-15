class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #init res
        res = 0
        #init left, right
        left, right = 0, len(heights)-1
        while left < right:
            #calc area which is right - left * max height
            print(left, right)
        
            area = (right-left) * min(heights[left], heights[right]) 
            
            res = max(res, area)
            #if left shorter than right increment left
            if heights[left] < heights[right]:
                left += 1

            #if right decrement
            else:
                right -= 1

        #return max 
        return res