class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        #for each number in nums
        for n in nums:
            #next permutations
            nextPerms = []
            # each perm in our permutations list
            for p in perms:
                #for each item in the range of a permutation
                for i in range(len(p)+1):
                    #copy it, insert the number at idx i
                    #add the copy to next perm list
                    permCopy = p.copy()
                    permCopy.insert(i,n)
                    nextPerms.append(permCopy)
            #Set next perms to result
            perms = nextPerms
        return perms
