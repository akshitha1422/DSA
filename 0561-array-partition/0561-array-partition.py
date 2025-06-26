class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        total=0
        while i+1<len(nums):
            curr=min(nums[i],nums[i+1])
            total+=curr
            i=i+2
        return total