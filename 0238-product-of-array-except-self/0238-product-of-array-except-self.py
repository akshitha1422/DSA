class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[0]*len(nums)
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            suf[i]=suf[i+1]*nums[i+1]

        for i in range(len(nums)):
            prod[i]=pre[i]*suf[i]
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