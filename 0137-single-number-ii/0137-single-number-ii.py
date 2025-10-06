class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1
        for n,f in freq.items():
            if f==1:
                return n