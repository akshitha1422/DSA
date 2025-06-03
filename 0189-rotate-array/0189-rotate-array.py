class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        if k>len(nums):
            k=k-len(nums)
        for i in range(k):
            a=nums[-1]
            nums.insert(0,a)
            del nums[-1]
