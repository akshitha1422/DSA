class Solution:
    def isValid(self, s: str) -> bool:
        syb={')':'(','}':'{',']':'['}
        st=[]
        for i in s:
            if i in syb.values():
                st.append(i)
            elif i in syb.keys():
                if st and st[-1]==syb[i]:
                    st.pop()
                else:
                    return False
        if len(st)!=0:
            return False
        return True