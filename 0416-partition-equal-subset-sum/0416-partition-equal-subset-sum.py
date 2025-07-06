class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        memo={}
        if sum(nums)%2==1:
            return False
        half=sum(nums)//2
        def helper(n,half):
            if half==0:
                return True
            if n==0:
                return False
            if (n,half) in memo:
                return memo[(n,half)]
            if nums[n-1]<=half:
                memo[(n,half)]=helper(n-1,half-nums[n-1]) or helper(n-1,half)
            else:
                memo[(n,half)]=helper(n-1,half)
            return memo[(n,half)]
        return helper(n,half)