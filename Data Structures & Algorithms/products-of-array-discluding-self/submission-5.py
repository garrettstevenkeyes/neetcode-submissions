class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
    #            i  
        # pre = 8
        # post = 1          
        #  res = [1,1,2,8]
        #             
        # 
        
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            # apply prefix
            res[i] *= prefix
            #multiply by num and continue
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res