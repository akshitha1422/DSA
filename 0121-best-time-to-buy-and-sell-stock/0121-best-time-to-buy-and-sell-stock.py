class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         max_profit=max(max_profit,prices[j]-prices[i])
        # return max_profit
        max_profit=0
        mini=float('inf')
        for i in prices:
            if i<mini:
                mini=i
            else:
                max_profit=max(max_profit,i-mini)
        return max_profit