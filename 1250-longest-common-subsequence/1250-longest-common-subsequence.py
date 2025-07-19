class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if text1[n-1]==text2[m-1]:
                memo[(n,m)]=1+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n-1,m),helper(n,m-1))
            return memo[(n,m)]
        return helper(n,m)