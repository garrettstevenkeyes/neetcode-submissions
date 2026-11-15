class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #init res list
        res = [1] * len(nums)
        
# [1, 1, 1, 1]

        #iterate
        prefix = 1
        for i in range(len(nums)):
            #apply to res
            res[i] *= prefix
            #update prefix
            prefix *= nums[i]

        postfix = 1
        #reverse iterate
        for i in range(len(nums)-1, -1, -1):
            #apply to res
            res[i] *= postfix
            #update prefix
            postfix *= nums[i]
        
        return res