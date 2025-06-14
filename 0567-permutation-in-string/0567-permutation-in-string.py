class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # from collections import Counter
        # freq=Counter(s1)
        # lt=len(s1)
        # i=0
        # while i<=len(s2)-lt:
        #     window=s2[i:i+lt]
        #     win_c=Counter(window)
        #     if freq==win_c:
        #         return True
        #     i+=1
        # return False

        from collections import Counter
        freq=Counter(s1)
        lt=len(s1)
        window=s2[:lt]
        win_c=Counter(window)
        if freq==win_c:
            return True
        for i in range(lt,len(s2)):
            start=s2[i-lt]
            end=s2[i]
            win_c[start]-=1
            win_c[end]+=1
            if win_c[start]==0:
                del win_c[start]
            if freq==win_c:
                return True
        return False