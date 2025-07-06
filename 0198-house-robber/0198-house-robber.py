class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        cap=sum(nums)
        def helper(n):
            if n>=len(nums):
                return 0
            if n in memo:
                return memo[n]
            memo[n]=max(nums[n]+helper(n+2),helper(n+1))
            return memo[n]
        return helper(0)