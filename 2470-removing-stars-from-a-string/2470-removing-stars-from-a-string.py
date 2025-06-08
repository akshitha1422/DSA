class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        i=0
        while i<len(s):
            if s[i]!='*':
                st.append(s[i])
            elif s[i]=='*':
                st.pop()
            i+=1
        return ''.join(st)