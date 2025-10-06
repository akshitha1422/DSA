class Solution:
    def hammingWeight(self, n: int) -> int:
        num_bit=bin(n)
        return str(num_bit).count('1')