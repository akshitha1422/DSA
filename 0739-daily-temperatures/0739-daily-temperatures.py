class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        st=[]
        for i,temp in enumerate(temperatures):
            while st and temperatures[i]>temperatures[st[-1]]:
                idx=st.pop()
                res[idx]=i-idx
            st.append(i)
        return res