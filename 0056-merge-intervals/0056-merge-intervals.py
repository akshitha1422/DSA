class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        st=[intervals[0]]
        for val in intervals[1:]:
            last=st[-1]
            if val[0]<=last[1]:
                last[1]=max(val[1],last[1])
            else:
                st.append(val)
        return st