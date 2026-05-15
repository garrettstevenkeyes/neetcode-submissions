# Brainstorm
# [3,4,5,6,1,2] 1=t
#  a
#.     m
#.           b
# define start,end and middle points
# check rules:
# 1. if the mid number equals the target return it
# 2. determine which sorted portion you are in left or right
# 3. if the left number is less than the mid, turn is on the right
#       if target is greater than the left and less than the mid move left
#       else move right 
# 4. if turn is on the left
#       if target greater than the mid and less than the right number
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)-1
        while a <= b:
            #1
            mid = (a + b) // 2
            
            if nums[mid] == target:
                return mid
            #2
            if nums[a] <= nums[mid]:
                #3
                if target >= nums[a] and target < nums[mid]:
                    b = mid - 1
                else:
                    a = mid + 1
            else:
                if target <= nums[b] and target > nums[mid]:
                    a = mid + 1
                else:
                    b = mid - 1
        return -1        
