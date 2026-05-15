class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #init a res list
        res = []
        #init a dfs function
        #should take a subset and an index
        def dfs(subset, idx):
            #base case is index is eol
            if idx == len(nums):
                #add num at index to the subset 
                res.append(subset)
                return

            # call the dfs
            dfs(subset + [nums[idx]], idx + 1)
            #remove the num
            #call the dfs
            dfs(subset, idx + 1)

        #call if with empty list and 0 idx
        dfs([], 0)

        return res


        
        