class Solution:
    def frequencySort(self, s: str) -> str:
        res=''
        from collections import Counter
        freq=Counter(s)
        sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for i,v in sorted_items:
            for _ in range(v):
                res+=i
        return res