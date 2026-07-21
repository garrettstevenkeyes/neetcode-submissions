class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        #  l
        #     r
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            else:
                l = r
            r += 1
        return maxProfit