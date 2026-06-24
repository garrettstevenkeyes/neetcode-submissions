class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMatches = {}
        #for each number get target - num
        #if that is in our seen dict, return it
        #otherwise save it in with idx as value
        for i in range(len(nums)):
            matchVal = target - nums[i]
            if matchVal in numMatches:
                return [numMatches[matchVal], i]
            else:
                numMatches[nums[i]] = i