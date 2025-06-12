class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import defaultdict
        sym=defaultdict(int)
        length=0
        for i in nums:
            if i not in sym:
                sym[i]=1
            else:
                sym[i]+=1
        for i in sym:
            if (i+1) in sym:
                new_len=sym[i]+sym[i+1]
                length=max(length,new_len)
        return length