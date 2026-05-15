#Brainstorm
# Time O(N)
# Space O(1)

#Plan
#1.init pointers on each side
#2.create a mid point
#3.if 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            #get mid point
            mid = (l + r) // 2

            #see if it equals the target
            if target == nums[mid]:
                return mid

            #left portion ascending and doesnt contain rotation
            if nums[l] <= nums[mid]:
                #if our target is greater than the midpoint
                #or less than the left point
                #move right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                #otherwise move left
                else:
                    r = mid - 1
            
            #right portion ascending and doesnt contain rotation
            else:
                #if our target is less than the midpoint
                #or greater than the right point
                #move left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                #otherwise move right
                else:
                    l = mid + 1
        #return default value
        return -1
