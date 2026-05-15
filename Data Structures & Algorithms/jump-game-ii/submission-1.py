#Brainstorm
# minJumps = inf
# [2,4,1,1,1,1]
#  l
#  r
#  l = 0, r=0
#  farthest = 2
# 
class Solution:
    def jump(self, nums: List[int]) -> int:
        #init the res
        res = 0
        #init the left and right pointers for our window
        r, l = 0, 0
        #while our right pointer is less than the 
        #end of the nums list
        while r < len(nums)-1:
            #init the farthest jump we can make
            farthest = 0
            #for each number in the window
            for i in range(l, r+1):
                #calculate the farthest jump we can make
                #which i the current index + the number at the index 
                farthest = max(farthest, i + nums[i])
            #if its a number > 0 which is guaranteed
            #the smallest jump is 1 so move l to
            #r + 1
            l = r + 1
            #move r to the farthest jump we can take
            r = farthest
             # add one to our res jumps
            res += 1
        return res
