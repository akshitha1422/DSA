class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                st.append(int(i))
            else:
                val1=st.pop()
                val2=st.pop()
                if i=='+':
                    st.append(val1+val2)
                elif i=='-':
                    st.append(val2-val1)
                elif i=='*':
                    st.append(val1*val2)
                else:
                    st.append(int(val2/val1))
        return st[-1]