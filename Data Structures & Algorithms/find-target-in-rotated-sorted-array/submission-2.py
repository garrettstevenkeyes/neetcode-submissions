#Brainstorm
# Time O(N)
# Space O(1)

#Plan
#1.init pointers on each side
#2.create a mid point
#3.if 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            #get mid point
            mid = (start + end) // 2

            #see if it equals the target
            if target == nums[mid]:
                return mid

            #left sorted portion
            if nums[start] <= nums[mid]:
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
