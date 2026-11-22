class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #iterate over nums
        for i in range(len(nums)-2):
            #check if current number equals previous
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #check if nums[i] > 0
            if nums[i] > 0:
                break

            start, end = i+1, len(nums)-1
            #look through start and end window
            while start < end:    
                total = nums[i] + nums[start] + nums[end]
                #check start and end
                if total > 0:
                    end -= 1

                elif total < 0:
                    start += 1

                else:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                
                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                    while start < end and end < len(nums)-1 and nums[end] == nums[end+1]:
                        end -= 1

        return res
