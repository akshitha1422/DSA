class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        st=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                st.append(matrix[i][j])
        st.sort()
        return st[k-1]