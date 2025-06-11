class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=set()
        i=0
        max_val=0
        for j in range(len(s)):
            while s[j] in sub:
                sub.remove(s[i])
                i+=1
            sub.add(s[j])
            max_val=max(max_val,j-i+1)
        return max_val