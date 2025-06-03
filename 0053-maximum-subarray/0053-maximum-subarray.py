class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=current=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],current+nums[i])
            max_sum=max(max_sum,current)
        return max_sum
