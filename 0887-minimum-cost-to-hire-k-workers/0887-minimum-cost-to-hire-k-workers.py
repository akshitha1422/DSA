class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers=sorted([(w / q, q) for q, w in zip(quality, wage)])
        max_heap=[]
        qual=0
        min_cost=float('inf')
        for ratio,q in workers:
            heapq.heappush(max_heap,-q)
            qual+=q
            if len(max_heap)>k:
                qual+=heapq.heappop(max_heap)
            if len(max_heap)==k:
                min_cost=min(min_cost,qual*ratio)
        return min_cost