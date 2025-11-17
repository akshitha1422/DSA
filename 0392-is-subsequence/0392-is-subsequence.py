class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s):
            if s[i] in t:
                j=t.index(s[i])
                t=t[j+1:]
                i+=1
            else:
                return False
        return True