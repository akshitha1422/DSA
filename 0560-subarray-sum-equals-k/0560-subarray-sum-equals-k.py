class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        curr=0
        count=0
        for n in nums:
            curr+=n
            if (curr-k) in prefix_count:
                count+=prefix_count[curr-k]
            prefix_count[curr]+=1
        return count