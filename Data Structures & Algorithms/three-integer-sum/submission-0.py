class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx in range(len(nums)):
            if ((idx > 0) and (nums[idx] == nums[idx -1])):
                #do not count it
                continue
            
            l, r = idx+1, len(nums)-1
            while l < r:
                threeSome = nums[idx] + nums[l] + nums[r]
                if threeSome > 0:
                    r -= 1
                elif threeSome < 0:
                    l += 1
                else:
                    res.append([nums[idx],nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


