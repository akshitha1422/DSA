class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        st=[0]*len(nums)
        for i in range(len(nums)):
            st[i]=nums[i]**2
        return sorted(st)