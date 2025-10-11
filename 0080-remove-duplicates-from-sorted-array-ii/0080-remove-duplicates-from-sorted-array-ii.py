class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        w=2
        for r in range(2,len(nums)):
            if nums[r]!=nums[w-2]:
                nums[w]=nums[r]
                w+=1
        return w