class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        mini=float('inf')
        for i in prices:
            if i<mini:
                mini=i
            else:
                res=max(res,i-mini)
        return res