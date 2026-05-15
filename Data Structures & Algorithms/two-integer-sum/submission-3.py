class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i in range(len(nums)):
            cur = target - nums[i]

            if cur in sumDict:
                return [sumDict[cur], i]
            else:
                sumDict[nums[i]] = i