class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b!=0:
            sum_=(a^b)& mask
            carry=((a&b)<<1)& mask
            a,b=sum_,carry
        if a<=0x7FFFFFFF:
            return a
        return a-(1<<32)