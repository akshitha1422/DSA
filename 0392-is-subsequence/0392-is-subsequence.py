class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=0
        s2=0
        n=len(t)
        while s1<len(s):
            if s[s1] in t:
                ind=t.index(s[s1])
                t=t[ind+1:]
                s1+=1
            else:
                return False
        return True

