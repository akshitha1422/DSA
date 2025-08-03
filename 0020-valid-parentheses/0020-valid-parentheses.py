class Solution:
    def isValid(self, s: str) -> bool:
        count=0
        sym={'(':')','{':'}','[':']'}
        st=[]
        for i in s:
            if i in sym.keys():
                st.append(i)
            elif i in sym.values():
                if not st or sym[st.pop()]!=i:
                    return False
        return len(st)==0