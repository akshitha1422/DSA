class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        freq=Counter(words)
        st=[]
        for word,val in freq.items():
            heapq.heappush(st,(-val,word))
        res=[]
        for _ in range(k):
            val,word=heapq.heappop(st)
            res.append(word)
        return res