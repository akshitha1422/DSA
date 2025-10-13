class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        extended=colors+colors[:k-1]
        res=0
        curr=1
        for i in range(len(extended)-1):
            if extended[i]!=extended[i+1]:
                curr+=1
            else:
                curr=1
            if curr>=k and i-k+1<n:
                res+=1
        return res