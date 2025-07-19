class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        memo={}
        def helper(n,m):
            if m==0:
                return 1
            if n==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if s[n-1]==t[m-1]:
                memo[(n,m)]=helper(n-1,m-1)+helper(n-1,m)
            else:
                memo[(n,m)]=helper(n-1,m)
            return memo[(n,m)]
        return helper(n,m)
