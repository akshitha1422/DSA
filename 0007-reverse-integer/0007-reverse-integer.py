class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign=1
        if x<0:
            sign*=-1
            x=x*-1
        st=[]
        while x>0:
            ls=x%10
            st.append(str(ls))
            x=x//10
        r1=''.join(st)
        res=int(r1)*sign
        if res<INT_MIN or res>INT_MAX:
            return 0
        else:
            return res