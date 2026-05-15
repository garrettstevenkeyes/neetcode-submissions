class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            #if we have gone out of the range of the list
            #add subset copy to res
            #and return
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            #create two possibilities, one where we include the number
            #and a second where we don't include the number
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
