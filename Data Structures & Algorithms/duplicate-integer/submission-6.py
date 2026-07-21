class Solution:
    #if a value appears more than once the number of items will decrease when turned into a set
    #convert and compare the two. If the counts != there was a duplicate 
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))