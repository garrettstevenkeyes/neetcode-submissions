class Solution:
    # Time O(N * log N)
    # Space O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort num list
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            #duplicate check
            if (i > 0) and nums[i] == nums[i-1]:
                continue
            
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
            
