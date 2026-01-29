class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st={}
        for i in range(len(nums)):
            if (target-nums[i]) in st:
                return [i,st[(target-nums[i])]]
            else:
                st[nums[i]]=i