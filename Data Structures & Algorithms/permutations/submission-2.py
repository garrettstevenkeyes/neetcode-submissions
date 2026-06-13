class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #init result
        res = []
        #dfs , take path and idx
        def dfs(path):
            #if the path is the length of the num list add it
            if len(path) == len(nums):
                res.append(path)
                return 
            
            #if the number is not in the path add it and call
            for num in nums:
                if num not in path:
                    dfs(path + [num])

        dfs([])
        return res