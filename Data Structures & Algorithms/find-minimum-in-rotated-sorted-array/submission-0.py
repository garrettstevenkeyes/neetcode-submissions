class Solution:
    def findMin(self, nums: List[int]) -> int:
            
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            # If the subarray is already sorted
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            # Check if we are in the left sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res