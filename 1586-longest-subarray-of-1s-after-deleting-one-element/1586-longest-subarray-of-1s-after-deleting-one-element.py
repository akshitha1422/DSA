class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        left=0
        zeros=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            count=max(count,right-left)
        return count
