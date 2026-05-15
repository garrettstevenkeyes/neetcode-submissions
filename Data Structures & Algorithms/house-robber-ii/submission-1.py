class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #we need to create a 2d cache
        #to account for first house robbed
        #or skipped
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i ==len(nums) -1):
                return 0
            #if the house num and the flag value in cache
            #then return the val
            if memo[i][flag] != -1:
                return memo[i][flag]

            #save the max into the cache
            memo[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag or (i==0)))
            return memo[i][flag]
        #call if for the first and second value
        return max(dfs(0, True), dfs(1, False))