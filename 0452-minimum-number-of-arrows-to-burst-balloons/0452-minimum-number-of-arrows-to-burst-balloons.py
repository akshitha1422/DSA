class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count=1
        prev=points[0][1]
        for point in points:
            if point[0]>prev:
                count+=1
                prev=point[1]
        return count
                
        # points.sort(key=lambda x:x[1])
        # res=[]
        # res.append(points[0])
        # for point in points:
        #     if res[-1][1]>=point[0]:
        #         res[-1][0]=min(point[0],res[-1][0])
        #         res[-1][1]=min(point[1],res[-1][1])
        #     else:
        #         res.append(point)
        # return len(res)