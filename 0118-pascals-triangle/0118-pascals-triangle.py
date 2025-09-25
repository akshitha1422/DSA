class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        st=[[1]]
        for _ in range(numRows-1):
            arr=st[-1]
            row=[1]
            for i in range(len(arr)-1):
                s=arr[i]+arr[i+1]
                row.append(s)
            row.append(1)
            st.append(row)
        return st