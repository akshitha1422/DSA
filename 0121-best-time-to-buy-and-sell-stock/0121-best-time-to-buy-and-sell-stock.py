class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        mini=float('inf')
        for i in prices:
            if i<mini:
                mini=i
            else:
                max_profit=max(max_profit,i-mini)
        return max_profit