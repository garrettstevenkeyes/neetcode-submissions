class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numStore = {}
        for i in range(len(nums)):
            #get target minus num (compliment)
            compliment = target - nums[i]
            #if compliment in numstore return [it, curr]
            if compliment in numStore:
                return [numStore[compliment], i]
            #add to numStore by [compliment,idx]
            numStore[nums[i]] = i
        return []