class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx=nums.index(min(nums))
        new=nums[idx:]+nums[:idx]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if new[mid]==target:
                return (mid+idx)%len(nums)
            elif new[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1