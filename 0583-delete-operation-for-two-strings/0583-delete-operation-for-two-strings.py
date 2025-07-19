class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs=self.delop(word1,word2)
        return len(word1)+len(word2)-2*lcs
    def delop(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if word1[n-1]==word2[m-1]:
                memo[(n,m)]=1+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n-1,m),helper(n,m-1))
            return memo[(n,m)]
        return helper(n,m)