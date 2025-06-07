class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st1=[]
        st2=[]
        st=[]
        for i in range(0,len(word1)):
            st1.append(word1[i])
        for i in range(0,len(word2)):
            st2.append(word2[i])
        i=0
        while i<len(st1+st2):
            if len(st1)>0:
                st.append(st1[i])
                st1.pop(0)
            if len(st2)>0:
                st.append(st2[i])
                st2.pop(0)
        return ''.join(st)