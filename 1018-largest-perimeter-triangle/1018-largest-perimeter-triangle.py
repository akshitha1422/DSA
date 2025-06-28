class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        p=0
        i=0
        for i in range(len(nums)-2):
            if nums[i+2]+nums[i+1]>nums[i]:
                d=nums[i]+nums[i+1]+nums[i+2]
                p=max(p,d)
            else:
                continue
            i+1
        return p
