#Brainstorm
# Time O(N Log(N))
# Space O(N)
#Plan
#1. define res and sort list
#2. iterate over nums list
#3. if the num is > 0 it cant == 0 so break loop
#4. if == add to res list and move both in
#5. if too low, move right
#6. if too high move left
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1. define res and sort list
        res = []
        nums.sort()
        #2. iterate over nums list
        for i,n in enumerate(nums):
            #3. if the num is > 0 it cant == 0 so break loop
            if n > 0:
                break

            if i > 0 and n == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                #4. if == add to res list and move both in
                if (threeSum < 0):
                    l += 1
                #5. if too low, move right
                elif  (threeSum > 0):
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            
        return res
