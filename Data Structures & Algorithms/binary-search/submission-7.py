class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #init start and end
        start, end = 0, len(nums)-1
        #iterate until they pass each other
        while start <= end:
            #get mid point between the two,
            #check if equal, more or less than target
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            
        return -1
