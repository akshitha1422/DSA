class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        mini=float('inf')
        for p in prices:
            if p<mini:
                mini=p
            else:
                res=max(res,p-mini)
        return res