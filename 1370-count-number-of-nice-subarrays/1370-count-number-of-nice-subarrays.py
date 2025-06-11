class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        pre=defaultdict(int)
        pre[0]=1
        count=0
        odd=0
        for i in nums:
            if i%2==1:
                odd+=1
            count+=pre[odd-k]
            pre[odd]+=1
        return count




        # not optimal
        # count=0
        # for i in range(len(nums)):
        #     odd=0
        #     for j in range(i,len(nums)):
        #         if nums[j]%2==1:
        #             odd+=1
        #         if odd==k:
        #             count+=1
        #         elif odd>k:
        #             break
        # return count