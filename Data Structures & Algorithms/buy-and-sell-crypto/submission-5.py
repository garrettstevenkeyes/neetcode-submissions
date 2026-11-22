class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        #     s
        #.        e
        # 6
        res = 0
        start = 0
        end = 0

        while end < len(prices):
            if start == end:
                end += 1 
            
            elif prices[end] > prices[start]:
                res = max(res, (prices[end]-prices[start]))
                end += 1

            else:
                start += 1
                end = start

        return res
