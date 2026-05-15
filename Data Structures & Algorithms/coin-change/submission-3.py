class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        INF = float('inf')

        def helper(target: int) -> int:
            # base cases
            if target == 0:
                return 0
            if target < 0:
                return INF

            # memo
            if target in cache:
                return cache[target]

            # try taking each coin once and add 1 to count
            best = min(1 + helper(target - coin) for coin in coins)
            cache[target] = best
            return best

        res = helper(amount)
        return -1 if res == INF else res
