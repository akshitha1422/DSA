class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=[(t[0],t[1],i) for i,t in enumerate(tasks)]
        tasks.sort()
        res=[]
        available=[]
        time=0
        i=0
        while i<len(tasks) or available:
            while i<len(tasks) and tasks[i][0]<=time:
                que,pro,idx=tasks[i]
                heapq.heappush(available,(pro,idx))
                i+=1
            if available:
                pro,idx=heapq.heappop(available)
                time+=pro
                res.append(idx)
            else:
                time=tasks[i][0]
        return res
