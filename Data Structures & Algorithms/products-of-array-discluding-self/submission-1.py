class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(res)):
            res[i] = prefix * res[i]
            prefix = nums[i] * prefix
        
        postfix = 1
        for i in range(len(res)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = nums[i] * postfix

        return res