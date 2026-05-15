class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx in range(len(numbers)):
            neededNum = target - numbers[idx]
            if neededNum in hashmap:
                return [hashmap[neededNum]+1, idx+1]
            else:
                hashmap[numbers[idx]] = idx
        
