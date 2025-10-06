class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        if num<=0:
            return False
        while num%2==0:
            num>>=1
        return num==1