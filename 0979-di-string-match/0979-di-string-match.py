class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l=0
        h=len(s)
        ans=[]
        for i in range(len(s)):
            if s[i]=='I':
                ans.append(l)
                l+=1
            else:
                ans.append(h)
                h-=1
        ans.append(l)
        return ans