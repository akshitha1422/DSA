class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if str1[n-1]==str2[m-1]:
                memo[(n,m)]=1+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n-1,m),helper(n,m-1))
            return memo[(n,m)]
        helper(n,m)
        i=n
        j=m
        st=''
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                i-=1
                j-=1
                st=str1[i]+st
            elif memo.get((i-1,j),0)>memo.get((i,j-1),0):
                i-=1
                st=str1[i]+st
            else:
                j-=1
                st=str2[j]+st
        while i>0:
            i-=1
            st=str1[i]+st
        while j>0:
            j-=1
            st=str2[j]+st
        return st