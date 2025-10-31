class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count=float('inf')
        curr=0
        i=0
        for j in range(len(nums)):
            curr+=nums[j]
            while curr>=target:
                count=min(count,j-i+1)
                curr-=nums[i]
                i+=1
        return 0 if count==float('inf') else count