class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = {} 
        for num in nums:
            if num in numHash:
                return True
            else:
                numHash[num] = num
        
        return False
