class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7]
        #. s       
        #.   m   
        #        e

        start, end = 0, len(nums)-1
        while start < end:
            #if start is <= the mid go right
            mid = (start + end) // 2

            #if the right is bigger rotation is to the right
            #and go right
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        return nums[start]

