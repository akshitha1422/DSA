class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        cover=[]
        for i in range(len(ranges)):
            cover.append([i-ranges[i],i+ranges[i]])
        cover.sort(key=lambda x:x[0])
        taps=0
        end=0
        i=0
        while end<n:
            far=end
            while i<len(cover) and cover[i][0]<=end:
                far=max(far,cover[i][1])
                i+=1
            if far==end:
                return -1
            taps+=1
            end=far
        return taps