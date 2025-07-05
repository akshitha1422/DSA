class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        freq=Counter(arr)
        lucky=-1
        for i in arr:
            if freq[i]==i:
                lucky=max(lucky,i)
        return lucky