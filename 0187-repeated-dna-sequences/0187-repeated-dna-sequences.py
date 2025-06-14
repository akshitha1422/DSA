class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        st={}
        res=[]
        i=0
        while i<len(s)-9:
            j=i+10
            window=s[i:j]
            if window not in st:
                st[window]=1
            else:
                st[window]+=1
            i+=1
        for k,v in st.items():
            if v>1:
                res.append(k)
        return res