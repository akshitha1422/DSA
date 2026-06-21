class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sys={}
        for i in range(len(nums)):
            if target-nums[i] in sys:
                return [i,sys[target-nums[i]]]
            else:
                sys[nums[i]]=i