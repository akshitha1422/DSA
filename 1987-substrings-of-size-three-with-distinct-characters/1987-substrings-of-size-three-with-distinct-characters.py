class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i=0
        j=i+3
        count=0
        while j<=len(s):
            window=s[i:j]
            a=0
            for n in window:
                if window.count(n)==1:
                    a+=1
            if a==3:
                count+=1
            j+=1
            i+=1
        return count