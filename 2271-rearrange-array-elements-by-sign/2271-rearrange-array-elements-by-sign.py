class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        st=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(pos)):
            st.append(pos[i])
            st.append(neg[i])
        return st