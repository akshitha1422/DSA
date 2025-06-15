class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left=0
        right=len(nums)-1
        ind=[]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
            if nums[mid]==target:
                ind.append(mid)
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
            if nums[mid]==target:
                ind.append(mid)
        ind.sort()
        if not ind:
            return [-1,-1]
        if len(ind)==1:
            return [ind[0],ind[0]]
        return [ind[0],ind[-1]]