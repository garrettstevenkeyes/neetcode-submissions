class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #define our res
        res = []
        #define a var for our current list of numbers
        subset = []
        #do our dfs taking the index of the current space
        def dfs(i):
            #if our index is >= len of the number list
            if i >= len(nums):
                res.append(subset.copy())
                #add a copy to our result
                return

            #otherwise
            #add our current num to our current subset
            #do dfs traversal
            subset.append(nums[i])
            dfs(i+1)

            #remove the current num
            #do dfs traversal
            subset.pop()
            dfs(i+1)

        #call dfs on start index
        dfs(0)
        return res
