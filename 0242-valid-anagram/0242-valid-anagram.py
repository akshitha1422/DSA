class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        res=0
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in t:
            if i not in freq:
                return False
            else:
                freq[i]-=1
        for i in freq.values():
            res+=abs(i)
        return res==0
        # c1=Counter(s)
        # c2=Counter(t)
        # if c1==c2:
        #     return True
        # return False