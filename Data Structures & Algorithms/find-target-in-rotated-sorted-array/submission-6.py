class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        while s <= e:
            mid = (s + e)//2
            if nums[mid] == target:
                return mid
            if nums[s] <= nums[mid]:
                if nums[mid] < target or target < nums[s]:
                    s = mid + 1
                else:
                    e = mid -1
            else:
                if target < nums[mid] or target > nums[e]:
                    e = mid - 1
                else:
                    s = mid + 1
        return -1
