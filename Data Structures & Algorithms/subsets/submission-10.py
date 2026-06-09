class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #init res
        res = []
        #init dfs, params = idx, subset
        def dfs(idx, subset):
            # if idx hits len nums
            if idx == len(nums):
                #add to res
                res.append(subset)
                #return
                return
            #recurse with current num
            dfs(idx+1, subset + [nums[idx]])
            #recurse without current item
            dfs(idx +1, subset)
            
        #call dfs function
        dfs(0,[])
        #return result
        return res