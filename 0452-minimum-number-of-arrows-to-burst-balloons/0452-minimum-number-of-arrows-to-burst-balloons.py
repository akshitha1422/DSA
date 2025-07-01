class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count=1
        prev=points[0][1]
        for val in points[1:]:
            if val[0]>prev:
                count+=1
                prev=val[1]
        return count
                