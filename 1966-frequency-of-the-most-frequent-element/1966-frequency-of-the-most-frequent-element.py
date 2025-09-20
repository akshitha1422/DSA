class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=1
        l=0
        for r in range(1,len(nums)):
            diff=(nums[r]-nums[r-1])*(r-l)
            k-=diff
            while k<0:
                k+=nums[r]-nums[l]
                l+=1
            res=max(res,r-l+1)
        return res