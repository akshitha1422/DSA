class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        st=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            st[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            st[i]*=suffix
            suffix*=nums[i]
        return st