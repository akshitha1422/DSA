class Solution:
    # def __init__(self):
    #     self.items=[]
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        st=[]
        for n in nums:
            heappush(st,n)
            if len(st)>k:
                heappop(st)
        return st[0]
    