class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i=0
        max_val=0
        while i<len(nums):
            if nums[i] % 2 == 0 and nums[i]<=threshold:
                j=i
                while j<len(nums) and nums[j]<=threshold and nums[j]%2==(j-i)%2:
                    j+=1
                max_val=max(max_val,j-i)
                i=j
            else:
                i+=1
        return max_val
            