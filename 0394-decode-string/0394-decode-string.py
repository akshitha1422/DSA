class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        curr=''
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=='[':
                st.append((curr,num))
                curr=''
                num=0
            elif i==']':
                last, repeat = st.pop()
                curr = last + curr * repeat
            else:
                curr+=i
        return curr
                    