class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def helper(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(helper(i+1), helper(i+2))
            return cache[i]
        return min(helper(0), helper(1))