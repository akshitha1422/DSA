class Solution:
    def maxDifference(self, s: str) -> int:
        sym={}
        Max=float('-inf')
        Min=float('inf')
        for i in s:
            if i not in sym:
                sym[i]=1
            else:
                sym[i]=sym[i]+1
        for i in sym:
            if sym[i]%2==1:
                Max=max(Max,sym[i])
            if sym[i]%2==0:
                Min=min(Min,sym[i])
        return Max-Min