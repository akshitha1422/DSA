class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        count=defaultdict(int)
        for i in arr:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        return len(count.values())==len(set(count.values()))