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

        # prod=[1]*len(nums)
        # for i in range(len(nums)):
        #     res=1
        #     for j in range(i):
        #         res*=nums[j]
        #     for j in range(i+1,len(nums)):
        #         res*=nums[j]
        #     prod[i]=res
        # return prod