# [3,4,5,6,1,2]
# [4,5,0,1,2,3]
#. 
# check if the rotation is in the left or right
# if it is left move left
# if it is right move right

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r) // 2

            # check if the rotation is in the left or right
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]