class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        keys=sorted(freq,key=freq.get)
        return keys[-1]