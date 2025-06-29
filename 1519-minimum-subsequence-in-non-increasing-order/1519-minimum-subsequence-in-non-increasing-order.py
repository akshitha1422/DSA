class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sub=[]
        total=sum(nums)
        for i in nums:
            sub.append(i)
            if sum(sub)>total-sum(sub):
                return sub
                
        # while sum(sub)<=total-sum(sub):
        #     sub.append(nums[i])
        #     i+=1
        # return sub