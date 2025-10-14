class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for _ in range(32):
            res=(res<<1)|(n&1)
            n>>=1
        return res
        # s=str(bin(n)[2:])
        # s=s.zfill(32)
        # s=s[::-1]
        # return int(s,2)