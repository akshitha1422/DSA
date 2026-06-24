class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        sign=1
        if x<0:
            sign=-1
            s=s[1:]
        t=''
        for i in range(len(s)-1,-1,-1):
            t+=s[i]
        ans=sign*int(t)
        if ans<-(2**31) or (2**31-1)<ans:
            return 0
        return ans