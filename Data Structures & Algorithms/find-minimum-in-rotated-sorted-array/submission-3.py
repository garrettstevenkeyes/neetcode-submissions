class Solution:
    #[3,4,5,6,1,2]
    # l
    #     m
    #           r
    def findMin(self, nums: List[int]) -> int:
        s,e = 0, len(nums)-1
        while s < e:
            m = (s+e)//2
            if nums[m] > nums[e]:
                s = m + 1
            else:
                e = m
        return nums[s]