class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,6,7,1]
        #        i
        #.       j  
        #. 6

        l, r= 0, 1
        maxVal = 0

        while r < len(prices):
            #profit
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxVal = max(profit, maxVal)
            else:
                l = r
            r += 1
        return maxVal