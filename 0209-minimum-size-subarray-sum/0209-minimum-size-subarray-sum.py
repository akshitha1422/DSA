class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count=float('inf')
        i=0
        s=0
        for j in range(len(nums)):
            s+=nums[j]
            while s>=target:
                count=min(count,j-i+1)
                s-=nums[i]
                i+=1
        return 0 if count==float('inf') else count