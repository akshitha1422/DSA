class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        curr=0
        count=0
        for n in nums:
            curr+=n
            if curr-k in prefix:
                count+=prefix[curr-k]
            prefix[curr]+=1
        return count