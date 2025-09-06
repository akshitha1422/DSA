import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly=1
        heap=[1]
        seen={1}
        for _ in range(n):
            ugly=heapq.heappop(heap)
            for i in primes:
                nxt=ugly*i
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap,nxt)
        return ugly