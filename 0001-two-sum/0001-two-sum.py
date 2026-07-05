class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sym={}
        for i in range(len(nums)):
            if (target-nums[i]) in sym:
                return [sym[target-nums[i]],i]
            else:
                sym[nums[i]]=i