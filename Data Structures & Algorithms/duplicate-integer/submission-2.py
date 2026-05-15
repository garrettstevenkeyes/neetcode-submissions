class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashmap
        numberCount = {}
        #iterate through the list of nums
        #counting items
        for num in nums:
            #if its already been seen exit early
            if num in numberCount:
                return True
            else:
                numberCount[num] = 1
        #otherwise there are no duplicates
        return False