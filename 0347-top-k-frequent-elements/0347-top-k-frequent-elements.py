class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq=Counter(nums)
        st=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in st[:k]]