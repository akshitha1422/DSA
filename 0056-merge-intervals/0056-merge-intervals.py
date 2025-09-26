class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        res.append(intervals[0])
        for interval in intervals:
            arr=res[-1]
            if interval[0]<=arr[1]:
                res[-1][0]=min(res[-1][0],interval[0])
                res[-1][1]=max(res[-1][1],interval[1])
            else:
                res.append(interval)
        return res