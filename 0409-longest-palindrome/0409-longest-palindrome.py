class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        freq=Counter(s)
        length=0
        odd=False
        for i in freq.values():
            if i%2==0:
                length+=i
            else:
                if i!=1:
                    length+=i-1
                odd=True
        if odd==True:
            length+=1
        return length