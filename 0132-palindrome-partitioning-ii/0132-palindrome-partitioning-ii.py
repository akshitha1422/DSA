class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)

        ispal=[[False]*n for _ in range(n)]
        for i in range(n):
            ispal[i][i]=True
        for i in range(n-1):
            ispal[i][i+1]=(s[i]==s[i+1])
        for length in range(3,n+1):
            for i in range(n-length+1):
                j=i+length-1
                ispal[i][j]=(s[i]==s[j] and ispal[i+1][j-1])


        dp=[0]*n
        for i in range(n):
            if ispal[0][i]:
                dp[i]=0
            else:
                dp[i]=float('inf')
                for j in range(1,i+1):
                    if ispal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        return dp[n-1]