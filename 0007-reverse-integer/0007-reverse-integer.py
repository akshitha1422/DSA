class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        final=''
        exp=0
        sign=1
        if x>=0:
            sign=sign*1
        else:
            sign=sign*(-1)
            x=x*(-1)
        while x>0:
            a=x%10
            final=final+str(a)
            x=x//10
            exp+=1

        if len(final)>0:
            final=int(final)
        else:
            final=0
        
        if final>INT_MAX or INT_MIN>final:
            final=0
        return final*sign