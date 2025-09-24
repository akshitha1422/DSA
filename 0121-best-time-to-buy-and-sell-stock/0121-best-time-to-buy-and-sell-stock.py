class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=float('inf')
        total=0
        for price in prices:
            left=min(left,price)
            total=max(total,price-left)
        return total