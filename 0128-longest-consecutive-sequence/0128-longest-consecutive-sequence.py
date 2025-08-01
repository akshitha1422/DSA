class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count=1
        curr=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]+1==nums[i+1]:
                curr+=1
            else:
                count=max(count,curr)
                curr=1
        return max(count,curr)