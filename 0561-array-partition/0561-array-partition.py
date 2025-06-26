class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # i=0
        # total=0
        # while i+1<len(nums):
        #     total+=nums[i]
        #     i=i+2
        # return total
        return sum(nums[::2])