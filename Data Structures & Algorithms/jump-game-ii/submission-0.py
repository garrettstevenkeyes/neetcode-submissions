#Brainstorm
# minJumps = inf
# [2,4,1,1,1,1]
#  i
#

class Solution:
    def jump(self, nums: List[int]) -> int:
        #minimum number of jumps
        res = 0
        l = r = 0
        #iterate to the right
        while r < len(nums) - 1:
            #our farthest possible jump
            farthest = 0
            #for each number from left to right
            for i in range(l, r + 1):
                #farthest is cur indx + number at that spot or max
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
