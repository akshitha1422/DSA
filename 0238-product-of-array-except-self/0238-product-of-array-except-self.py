class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[0]*len(nums)
        pre=1
        for i in range(len(nums)):
            prod[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(len(nums)-1,-1,-1):
            prod[i]*=suf
            suf*=nums[i]
        return prod


        # prod=[1]*len(nums)
        # for i in range(len(nums)):
        #     res=1
        #     for j in range(i):
        #         res*=nums[j]
        #     for j in range(i+1,len(nums)):
        #         res*=nums[j]
        #     prod[i]=res
        # return prod