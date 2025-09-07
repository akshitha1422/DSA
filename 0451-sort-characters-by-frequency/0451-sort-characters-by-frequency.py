import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        #same
        res=''
        from collections import Counter
        freq=Counter(s)
        st=[]

        for i,v in freq.items():
            heapq.heappush(st,(-v,i))
        while st:
            i,v=heapq.heappop(st)
            res+=-i*v
        return res

        # sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        # for i,v in sorted_items:
        #     res+=i*v
        # return res