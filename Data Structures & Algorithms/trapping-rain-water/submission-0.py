class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        #iterate through the height list left to right 
        #get the max values to the left
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        #Iterate right to left and get max values right to left
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        # get the min between the nums and then subtract height[i]
        #that is how much water it can hold
        for i in range(len(height)):
            calc = min(leftMax[i], rightMax[i]) - height[i]
            if (calc) > 0:
                res += calc
        
        return res
        #add it to total