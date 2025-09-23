class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        st=[[1]]
        for _ in range(1,rowIndex+1):
            arr=st[-1]
            row=[1]
            for i in range(len(arr)-1):
                s=arr[i]+arr[i+1]
                row.append(s)
            row.append(1)
            st.append(row)
        return st[-1]