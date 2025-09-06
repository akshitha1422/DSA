class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        freq=Counter(tasks)
        count=0
        max_freq=max(freq.values())
        for i in freq.values():
            if i==max_freq:
                count+=1
        cal=(max_freq-1)*(n+1)+count
        return max(len(tasks),cal)