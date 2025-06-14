class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ''

        freq=Counter(t)
        min_len=float('inf')
        min_str=''
        i=0
        win=Counter()
        req=len(freq)
        formed=0
        for j in range(len(s)):
            win[s[j]]+=1
            if s[j] in freq and win[s[j]]==freq[s[j]]:
                formed+=1
            while formed==req:
                if (j-i+1)<min_len:
                    min_len=(j-i+1)
                    min_str=s[i:j+1]
                win[s[i]]-=1
                if s[i] in freq and win[s[i]]<freq[s[i]]:
                    formed-=1
                i+=1
        return min_str