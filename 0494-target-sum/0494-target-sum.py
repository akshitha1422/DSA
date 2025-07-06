class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        if abs(target)>sum(nums) or (target+sum(nums))%2==1:
            return 0
        cap=(target+sum(nums))//2
        def helper(n,cap):
            if n==0:
                if cap==0:
                    return 1
                else:
                    return 0
            if (n,cap) in memo:
                return memo[(n,cap)]
            if nums[n-1]<=cap:
                memo[(n,cap)]=helper(n-1,cap-nums[n-1])+helper(n-1,cap)
            else:
                memo[(n,cap)]=helper(n-1,cap)
            return memo[(n,cap)]
        return helper(n,cap)