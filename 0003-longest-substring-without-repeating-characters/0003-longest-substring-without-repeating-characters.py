class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sym=set()
        res=0
        i=0
        for j in range(len(s)):
            while s[j] in sym:
                sym.remove(s[i])
                i+=1
            sym.add(s[j])
            res=max(res,len(sym))
        return res