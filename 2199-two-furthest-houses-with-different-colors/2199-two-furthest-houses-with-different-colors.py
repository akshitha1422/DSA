class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_val=0
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=colors[0]:
                max_val=max(max_val,i)
                break
        for i in range(len(colors)):
            if colors[i]!=colors[len(colors)-1]:
                max_val=max(max_val,len(colors)-1-i)
                break
        return max_val