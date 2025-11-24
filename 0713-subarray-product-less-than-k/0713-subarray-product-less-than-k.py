class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        res=0
        left=0
        pro=1
        for right in range(len(nums)):
            pro*=nums[right]
            while pro>=k:
                pro//=nums[left]
                left+=1
            res+=right-left+1
        return res