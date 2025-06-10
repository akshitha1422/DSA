class Solution:
    def isPalindrome(self, x: int) -> bool:
        st1=[]
        st2=[]
        sign=1
        if x<0:
            sign*=-1
            x*=-1
            st1.append('-')
        while x>0:
            a=x%10
            st1.append(a)
            st2.insert(0,a)
            x=x//10
        if sign==-1:
            st2.append('-')
        return st1==st2