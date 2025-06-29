class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i=0
        total=0
        while i+2<len(cost):
            total+=cost[i]+cost[i+1]
            i+=3
        if i<len(cost):
            total+=sum(cost[i:])
        return total