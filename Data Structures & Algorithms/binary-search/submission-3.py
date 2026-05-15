class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx, endIdx = 0, len(nums) - 1
        while startIdx <= endIdx:
            mid = (startIdx + endIdx) // 2

            if nums[mid] > target:
                endIdx = mid - 1
            elif nums[mid] < target:
                startIdx = mid + 1
            else:
                return mid
        return -1
