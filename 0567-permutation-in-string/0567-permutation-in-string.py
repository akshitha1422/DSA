class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        freq=Counter(s1)
        to_see=freq
        lt=len(s1)
        i=0
        while i<=len(s2)-lt:
            j=i+lt
            window=s2[i:j]
            win_c=Counter(window)
            if freq==win_c:
                return True
            i+=1
        return False