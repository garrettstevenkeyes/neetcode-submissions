class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end)//2
            #check if the rotation is to the right
            if nums[mid] > nums[end]:
                start = mid + 1
            #left rotation
            elif nums[start] > nums[mid]:
                end = mid
            else:
                end = mid
        return nums[start]
#[4,5,0,1,2,3]
#    se       
