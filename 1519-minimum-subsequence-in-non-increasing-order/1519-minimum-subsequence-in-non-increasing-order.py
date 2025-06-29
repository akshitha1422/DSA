class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sub=[]
        total=sum(nums)
        i=0
        while sum(sub)<=total-sum(sub):
            sub.append(nums[i])
            i+=1
        return sub