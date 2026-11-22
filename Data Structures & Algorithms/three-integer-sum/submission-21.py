class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #sort the list
        nums.sort()
        
        for idx in range(len(nums)-2):
            # if the previous num equals the current one
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue
            
            if nums[idx] > 0:
                break

            start = idx + 1
            end = len(nums)-1
            while start < end:
                total = nums[idx] + nums[start] + nums[end]
                    
                if total > 0:
                    end -= 1
                    
                elif total < 0:
                    start += 1
                
                else:
                    res.append([nums[idx], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                    while start < end and nums[end] == nums[end+1]:
                        end -= 1

        return res
            
