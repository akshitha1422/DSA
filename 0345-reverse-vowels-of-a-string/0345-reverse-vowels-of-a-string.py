class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=['a','e','i','o','u','A','E','I','O','U']
        st=[]
        for i in range(len(s)):
            if s[i] in vow:
                st.append(s[i])
        for i in range(len(s)):
            if s[i] in vow:
                a=st.pop()
                s=s[:i]+a+s[i+1:]
        return s