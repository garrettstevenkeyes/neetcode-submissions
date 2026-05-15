#Brainstorm
# Space O(1)
# Time O(N)
#Plan
# [1,2,0,1,0]
#          i  
# iterate from the end to the front
# in helper function(idx, numList)
#   if the num at whatever idx is equal to or less than
#   the distance from the end there are enough moves 
#   else if we have already seen the space is true 
class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return True if goal == 0 else False
                