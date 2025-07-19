class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        lcs=self.LCS(s1,s2)
        ch=0
        for i in range(len(s1)):
            ch+=ord(s1[i])
        for j in range(len(s2)):
            ch+=ord(s2[j])
        return ch-2*lcs
    def LCS(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if s1[n-1]==s2[m-1]:
                memo[(n,m)]=ord(s1[n-1])+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n-1,m),helper(n,m-1))
            return memo[(n,m)]
        return helper(n,m)