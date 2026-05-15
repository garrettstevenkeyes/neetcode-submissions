#Plan
#define res and sort
# loop over list
# if num > 0 exit early
# if num is the same as the previous continue
# l,r pointers
# if threeSum < 0 move left
# while number at l == l-1 incriment it
# elif threeSum > 0 move right
#else add to res and increment left and right

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #define res and sort
        res = []
        nums.sort()
        # loop over list
        for i, n in enumerate(nums):
            # if num > 0 exit early
            if n > 0:
                break
            # if num is the same as the previous continue
            if (i > 0) and (n == nums[i-1]):
                continue
            # l,r pointers
            l,r = i+1, len(nums)-1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                # if threeSum < 0 move left
                if threeSum < 0:
                    l += 1
                    
                # elif threeSum > 0 move right
                elif threeSum > 0:
                    r -= 1
                   
                #else add to res and increment left and right
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # while number at l == l-1 incriment it
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
        