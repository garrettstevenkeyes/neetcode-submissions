class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset, idx):
            #base case, our subset equals len of nums
            if idx == len(nums):
                res.append(subset)
                return
            #include the current num in the subset
            dfs(subset + [nums[idx]], idx + 1)
            #skip the current num in the subset
            dfs(subset, idx + 1)
        
        dfs([], 0)
        return res