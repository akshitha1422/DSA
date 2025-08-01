class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        n=len(nums)
        for i in freq.keys():
            if freq[i]>n//2:
                return i