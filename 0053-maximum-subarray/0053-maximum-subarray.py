class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=curr=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            total=max(total,curr)
        return total