class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        count=1
        curr=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                curr+=1
                count=max(count,curr)
            else:
                curr=1
        return count