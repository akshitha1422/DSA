class Solution:
    def reverseBits(self, n: int) -> int:
        s=str(bin(n)[2:])
        s=s.zfill(32)
        s=s[::-1]
        return int(s,2)