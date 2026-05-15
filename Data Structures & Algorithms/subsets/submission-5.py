class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #define res list
        res = []
        #define subset to be current one
        subset = []
        #define dfs
        def dfs(i):
        #input is the index
            #base case if i >= len(nums) then we are returning
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


        #call it on index 0
        #return a res
        dfs(0)
        return res