class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        equals=0
        freq={}
        for i in grid:
            t=tuple(i)
            freq[t]=freq.get(t,0)+1
        n=len(grid)
        for i in range(n):
            st=[]
            for j in range(n):
                st.append(grid[j][i])
            if tuple(st) in freq:
                equals+=freq[tuple(st)]
        return equals