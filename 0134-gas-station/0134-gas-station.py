class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        tank=0
        start=0
        total=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        if total>=0:
            return start
        else:
            return -1