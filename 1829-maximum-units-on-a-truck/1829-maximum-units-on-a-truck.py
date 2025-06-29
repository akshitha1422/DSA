class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        total=0
        for t,u in boxTypes:
            if truckSize>=t:
                total+=t*u
                truckSize-=t
            else:
                total+=truckSize*u
                break
        return total