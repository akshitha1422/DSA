class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        items=[[val[i],wt[i]] for i in range(len(val))]
        items.sort(key=lambda x: x[0]/x[1], reverse=True)
        res=0
        for i in range(len(val)):
            if items[i][1]<=capacity:
                res+=items[i][0]
                capacity-=items[i][1]
            else:
                res+=items[i][0]/items[i][1]*capacity
                break
        return res