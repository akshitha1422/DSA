class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind=nums.index(min(nums))
        new=nums[ind:]+nums[:ind]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if new[mid]==target:
                return (mid+ind)%len(nums)
            elif new[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1