class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, subset):
            #define base cases
            #if i is outside of the range add to res
            if sum(subset) == target:
                res.append(subset.copy())
                return 
            
            #if i is out of the range
            if sum(subset) > target or i >= len(nums):
                return
            
            #add to the subset
            #recurse
            subset.append(nums[i])
            helper(i, subset)

            #remove from the subset
            #this is to test both possibilities
            subset.pop()
            helper(i+1, subset)

        helper(0, [])
        return res


            

        