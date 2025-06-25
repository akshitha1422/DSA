class Solution:
    def jobSequencing(self, deadline, profit):
        def find(parent,x):
            if parent[x]!=x:
                parent[x]=find(parent,parent[x])
            return parent[x]
        def union(parent,x,y):
            parent[x]=y
        jobs=sorted(zip(profit,deadline),reverse=True)
        parent=[i for i in range(max(deadline)+1)]
        count=0
        total=0
        for p,d in jobs:
            aval=find(parent,d)
            if aval>0:
                union(parent,aval,aval-1)
                count+=1
                total+=p
        return [count,total]