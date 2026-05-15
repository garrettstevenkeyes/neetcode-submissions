class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #define a result
        res = []
        #Define recrusive helper, it takes i and our current num list
        def helper(i, curNums):
            # if the sum of our current num list = target
            # we will add a copy to the res and return
            if sum(curNums) == target:
                res.append(curNums.copy())
                return

            #if our current sum is greater than the target
            #or our index is over the limit return
            if sum(curNums) > target or i >=len(nums):
                return

            #add our current number at i to the curnumlist
            #call the helper on the same number, include the same
            curNums.append(nums[i])
            helper(i, curNums)

            #remove the current number from the curnumlist
            #call the helper on the next number 
            curNums.pop()
            helper(i+1, curNums)

        #call our recursion 
        helper(0,[])
        #return our result
        return res
