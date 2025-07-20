class Solution:
    def minInsertions(self, s: str) -> int:
        s2=s[::-1]
        lcs=self.LCS(s,s2)
        return len(s)-lcs
    def LCS(self, s: str, s2:str) -> int:
        s2=s[::-1]
        n=m=len(s)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if s[n-1]==s2[m-1]:
                memo[(n,m)]=1+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n-1,m),helper(n,m-1))
            return memo[(n,m)]
        return helper(n,m)