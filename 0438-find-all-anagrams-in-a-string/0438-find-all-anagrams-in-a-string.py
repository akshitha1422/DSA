class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        st=[]
        p=sorted(p)
        for i in range(0,len(s)-n+1):
            window=s[i:i+n]
            if sorted(window)==p:
                st.append(i)
        return st