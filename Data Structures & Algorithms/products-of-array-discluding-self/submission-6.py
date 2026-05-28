class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,1,2,8]
        #prefix = 1
        #postfix = 1
        prefix = 1
        res = [1] * len(nums)

        #prefix x res
        #prefix x num
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res