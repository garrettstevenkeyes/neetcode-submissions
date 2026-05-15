class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, subset):
            #define base cases
            if len(subset) == k:
                res.append(subset.copy())
                return 
            if i > n:
                return

            #do recursion
            subset.append(i)
            helper(i+1, subset)

            #explore other possibility
            subset.pop()
            helper(i+1, subset)
        helper(1,[])
        return res