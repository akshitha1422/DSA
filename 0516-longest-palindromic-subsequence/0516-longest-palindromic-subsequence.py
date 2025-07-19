class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2=s[::-1]
        n=len(s)
        m=len(s2)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if s[n-1]==s2[m-1]:
                memo[(n,m)]=1+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n,m-1),helper(n-1,m))
            return memo[(n,m)]
        return helper(n,m)
    def pal(s):
        lcs=self.longestPalindromeSubseq(s)
        return len(s)-lcs