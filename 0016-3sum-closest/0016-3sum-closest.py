class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float('inf')
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if abs(s-target)<abs(res-target):
                    res=s
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    return target
        return res