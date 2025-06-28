class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        st=[]
        for i,v in enumerate(nums):
            st.append((v,i))
        st.sort(key=lambda x:x[0], reverse=True)
        top=st[:k]
        top.sort(key=lambda x:x[1])
        st2=[]
        for i,n in top:
            st2.append(i)
        return st2