class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sym={}
        i=0
        count=0
        max_freq=0
        for j in range(len(s)):
            sym[s[j]]=sym.get(s[j],0)+1
            max_freq=max(max_freq,sym[s[j]])
            if (j-i+1)-max_freq>k:
                sym[s[i]]-=1
                i+=1
            count=max(count,j-i+1)
        return count