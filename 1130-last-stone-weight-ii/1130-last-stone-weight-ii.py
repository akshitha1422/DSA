class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        memo={}
        def helper(n,cap):
            if cap==0:
                return True
            if n==0:
                return stones[0]==cap
            if (n,cap) in memo:
                return memo[(n,cap)]
            not_take=helper(n-1,cap)
            take=False
            if stones[n]<=cap:
                take=helper(n-1,cap-stones[n])
            memo[(n,cap)]=take or not_take
            return memo[(n,cap)]
        min_val=float('inf')
        for s in range(sum(stones)//2+1):
            if helper(n-1,s):
                min_val=min(min_val,sum(stones)-2*s)
        return min_val
