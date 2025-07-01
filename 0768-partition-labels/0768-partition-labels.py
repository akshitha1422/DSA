class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={char:idx for idx,char in enumerate(s)}
        st=[]
        start=end=0
        for i,ch in enumerate(s):
            end=max(end,last[ch])
            if i==end:
                st.append(end-start+1)
                start=i+1
        return st