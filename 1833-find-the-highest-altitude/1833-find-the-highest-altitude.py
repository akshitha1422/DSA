class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        st=[]
        st.append(0)
        for i in range(len(gain)):
            alt=st[-1]+gain[i]
            st.append(alt)
        return max(st)