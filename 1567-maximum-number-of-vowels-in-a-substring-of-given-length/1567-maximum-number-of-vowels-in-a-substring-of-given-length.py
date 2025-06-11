class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sym=['a', 'e', 'i', 'o', 'u']
        window=s[:k]
        max_val=0
        for i in window:
            if i in sym:
                max_val+=1
        count=max_val
        for i in range(k,len(s)):
            if s[i] in sym:
                count+=1
            if s[i-k] in sym:
                count-=1
            max_val=max(max_val,count)
        return max_val