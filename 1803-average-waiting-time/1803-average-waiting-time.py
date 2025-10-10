class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total=0
        curr=0
        for arr,prep in customers:
            curr=max(curr,arr)+prep
            total+=curr-arr
        return total/len(customers)