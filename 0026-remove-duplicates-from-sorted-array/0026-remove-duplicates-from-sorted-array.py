class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        count=len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                nums.pop(i)
                count-=1
            else:
                seen.add(nums[i])
        return count