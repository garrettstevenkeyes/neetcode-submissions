class Solution:
    def jump(self, nums: List[int]) -> int:
        #init result vars
        minJumps = 0
        l, r = 0, 0

        #until we reach the end of the list iterate
        while r < len(nums)-1:
            farthest = 0
            #for each number in our window in the list
            for i in range(l, r + 1):
                #get the maximum value (furthest) we can jump
                farthest = max(farthest, i + nums[i])
            #we know the min move is + 1 because its guaranteed to reach the end
            #so left should be + 1
            l = r + 1
            #right should be + the maximum value
            r = farthest
            # increment our jump counter
            minJumps += 1
        
        return minJumps