class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #init start and end pointers
        start, end = 0, len(nums)-1
        #while the start is less than the end
        while start <= end:
            #init mid
            mid = (start + end) // 2
            #if mid equals the target return mid
            if target == nums[mid]:
               return mid 

            #if mid i greater than the target move end to mid-1
            elif nums[mid] > target:
                end = mid -1
            #if mid is less than the target move start to mid + 1
            else:
                start = mid + 1
        return -1