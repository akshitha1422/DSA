class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sub=[]
        sum_sub=0
        total=sum(nums)
        for i in nums:
            sum_sub+=i
            sub.append(i)
            if sum_sub>total-sum_sub:
                return sub

        # while sum(sub)<=total-sum(sub):
        #     sub.append(nums[i])
        #     i+=1
        # return sub