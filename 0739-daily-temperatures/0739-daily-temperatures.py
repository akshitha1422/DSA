class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        st=[]
        for i,temp in enumerate(temperatures):
            while st and temperatures[st[-1]]<temp:
                prev=st.pop()
                result[prev]=i-prev
            st.append(i)
        return result