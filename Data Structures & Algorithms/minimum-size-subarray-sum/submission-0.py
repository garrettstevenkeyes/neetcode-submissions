# nums = [1,2,1], target = 5
#.        L
#.            R
#
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, minLength, total = 0, float('inf'), 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minLength = min(minLength, R - L + 1)
                total -= nums[L]
                L += 1
                
        return 0 if minLength == float('inf') else minLength