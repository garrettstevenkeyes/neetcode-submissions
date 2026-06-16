class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, cache):
            #if you reach the top of the stairs
            if i >= n:
                return i == n
            #check the cache for the step
            if i in cache:
                return cache[i]
            #
            cache[i] = dfs(i+1, cache) + dfs(i+2, cache)
            return cache[i]
        return dfs(0, {})