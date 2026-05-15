class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6]
        #[1,1,1,1]
        #prefix = 1
        
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            #apply to res
            res[i] = res[i] * prefix
            #update prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            #apply to res
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        
        return res

