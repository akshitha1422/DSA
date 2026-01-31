class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq=[0]*(n+1)
        for i in nums:
            freq[i]+=1
        dup=miss=-1
        for i in range(1,n+1):
            if freq[i]==2:
                dup=i
            elif freq[i]==0:
                miss=i
        return [dup,miss]