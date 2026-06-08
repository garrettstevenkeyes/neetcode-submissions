class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset, idx):
            #base case if we hit end of list
            #add to result and return
            if idx == len(nums):
                res.append(subset)
                return

            #recurse including current num
            dfs(subset + [nums[idx]], idx + 1)
            #recurse excluding current num
            dfs(subset, idx + 1)
        #start with empty list and idx 0
        dfs([],0)
        return res