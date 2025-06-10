class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                st.append(int(i))
            else:
                v1=st.pop()
                v2=st.pop()
                if i=='+':
                    st.append(v2+v1)
                elif i=='-':
                    st.append(v2-v1)
                elif i=='*':
                    st.append(v2*v1)
                elif i=='/':
                    st.append(int(v2 / v1))
        return st[0]
