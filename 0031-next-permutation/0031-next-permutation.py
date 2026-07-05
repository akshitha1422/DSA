class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=len(nums)-2
        while left>=0 and nums[left]>=nums[left+1]:
            left-=1
        if left>=0:
            right=len(nums)-1
            while nums[right]<=nums[left]:
                right-=1
            nums[left],nums[right]=nums[right],nums[left]
        i,j=left+1,len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1