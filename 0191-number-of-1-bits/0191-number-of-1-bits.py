class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin=bin(n)
        return n_bin.count('1')