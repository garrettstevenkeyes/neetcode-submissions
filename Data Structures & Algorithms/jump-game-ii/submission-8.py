class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        # init res
        minJumps = 0
        #iterative right pointer
        while right < len(nums)-1:
            #define the longest jump as 0 to start
            longestJump = 0
            #get the furthest jump
            for i in range(left, right+1):
                longestJump = max(longestJump, nums[i])
            #move left 1 past right to min jump
            left = right + 1
            #move right to current + longest
            right = i + longestJump
            # add one to the minimum jumps
            minJumps += 1
        return minJumps