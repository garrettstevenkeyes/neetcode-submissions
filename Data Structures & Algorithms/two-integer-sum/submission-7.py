class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create hashmap
        numCounter = {}
        #iterate over list
        for i in range(len(nums)):
            num = nums[i]
            #take compliment = target-num
            compliment = target - num
            #if compliment in hashmap
            if compliment in numCounter:
                #return curidx and it
                return [numCounter[compliment], i]
            #else store curr number and idx
            else:
                numCounter[num] = i
