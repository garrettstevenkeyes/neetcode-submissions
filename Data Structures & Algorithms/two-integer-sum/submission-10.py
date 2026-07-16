class Solution:
    #structures = hashmap to stack vales seen at idx's
    #time O(N), one list traversal
    #space O(N), for save of list
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #init a dict
        seen = {}
        #traverse list, if target - cur val has been seen we return our answer
        #otherwise save current num and its idx
        for idx, num in enumerate(nums):
            neededNum = target - num
            if neededNum in seen:
                return [seen[neededNum], idx]
            else:
                seen[num] = idx
            

        

        