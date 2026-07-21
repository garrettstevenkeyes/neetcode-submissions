class Solution:
    #time O(N)
    #space O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate list, calc needed, check if its in seen dict, save if no, fetch if yes
        seen = {}
        for idx, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], idx]
            else:
                seen[num] = idx
        
        