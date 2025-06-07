class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left<right and s[left] not in vow:
                left+=1
            while left<right and s[right] not in vow:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return ''.join(s)




        # st=[]
        # for i in range(len(s)):
        #     if s[i] in vow:
        #         st.append(s[i])
        # for i in range(len(s)):
        #     if s[i] in vow:
        #         a=st.pop()
        #         s=s[:i]+a+s[i+1:]
        # return s