class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # res=bin(x^y)
        # return res.count('1')
        res=0
        while x>0 or y>0:
            res+=(x&1)^(y&1)
            x>>=1
            y>>=1
        return res