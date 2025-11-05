class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_bin=bin(n)[2:]
        s='1'*len(n_bin)
        num=int(n_bin,2)^int(s,2)
        return num