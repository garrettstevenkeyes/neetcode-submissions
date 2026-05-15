class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #init a result
        res = []
        #init subsets
        subset = []

        def dfs(i):
            #input is current subset
                #base case is the subset is the length of nums
                if i >= len(nums):
                    res.append(subset.copy())
                    return 

                # add the number to subset
                #call dfs 
                subset.append(nums[i])
                dfs(i+1)

                #remove the number
                #call dfs
                subset.pop()
                dfs(i+1)

        dfs(0)
        return res
        