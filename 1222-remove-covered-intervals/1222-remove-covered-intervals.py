class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        start=intervals[0][0]
        end=intervals[0][1]
        rem=0
        for val in intervals[1:]:
            if val[0]>=start and val[1]<=end:
                rem+=1
            else:
                start=val[0]
                end=val[1]
        return len(intervals)-rem