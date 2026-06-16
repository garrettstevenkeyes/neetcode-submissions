class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            #if you reach the top of the stairs
            if i >= n:
                return i == n
            #check the cache for the step
            if cache[i] != -1:
                return cache[i]
            #save to cache
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)