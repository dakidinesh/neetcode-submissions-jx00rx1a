class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        for r in range(1,len(prices)-1):
            if prices[r]>prices[l]:
                profit=max(profit,prices[r]-prices[l])
            else:
                l=r
        return profit