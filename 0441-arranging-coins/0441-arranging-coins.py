class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows=0
        i=1
        while n>0:
            if n>=i:
                rows+=1
                n-=i
            else:
                n-=i
            i+=1
        return rows