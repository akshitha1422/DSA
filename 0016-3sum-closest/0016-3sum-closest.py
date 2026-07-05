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
                sum=nums[i]+nums[left]+nums[right]
                if abs(target-sum)<abs(res-target):
                    res=sum
                elif sum<target:
                    left+=1
                elif sum>target:
                    right-=1
                else:
                    return target
        return res