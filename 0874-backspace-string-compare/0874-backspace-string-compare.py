class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1=[]
        st2=[]
        for i in range(len(s)):
            if st1 and s[i]=='#':
                st1.pop()
            else:
                st1.append(s[i])
        for j in range(len(t)):
            if st2 and t[j]=='#':
                st2.pop()
            else:
                st2.append(t[j])
        if '#' in st1:        
            st1.remove('#')
        if '#' in st2:
            st2.remove('#')
        if st1==st2:
            return True
        else:
            return False
        