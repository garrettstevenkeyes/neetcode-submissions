class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
        #        n s 
        #              e
        #init res
        res = []
        #iterate through
        nums.sort()
        for i in range(len(nums)-2):

            #if you are at the second item or >
            #and it is equal to the previous skip it
            if (i > 0) and nums[i] == nums[i-1]:
                continue
            
            #set left and right pointers
            left, right = i+1, len(nums)-1
            while left < right:
                #greater 
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1

                #less 
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                #equal
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res

            

