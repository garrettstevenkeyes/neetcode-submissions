class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #sort the list so its smallest to greatest
        nums.sort()
        perms = [[]]
        #for each num in nums
        for n in nums:
            #for each permutation in perms
            nextPerms = []
            for p in perms:
                for i in range(len(p)+1):
                    # Avoid inserting n after a duplicate n in the same position
                    #if there is more than one item in p
                    #and the item before equals n skip it
                    if i > 0 and p[i-1] == n:
                        break
                    permsCopy = p.copy()
                    permsCopy.insert(i,n)
                    nextPerms.append(permsCopy)
            perms = nextPerms
        return perms