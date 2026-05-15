#Brainstorm
# Time O(N)
# Space O(N)

#Plan
#1. create empty dict
#2. iterate the list
#3. get compliment by doing target - num 
#4. if compliment is in dict return [compliment, curIdx]
#5. else save compliment

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. create empty dict
        numPairs = {}
        #2. iterate the list
        for idx, num in enumerate(nums):
        #3. get compliment by doing target - num 
            compliment = target - num
        #4. if compliment is in dict return [compliment, curIdx]
            if compliment in numPairs:
                return [numPairs[compliment], idx]
        #5. else save compliment
            numPairs[num] = idx