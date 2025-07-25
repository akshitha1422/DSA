
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo={}
        def helper(s1,s2):
            if (s1,s2) in memo:
                return memo[(s1,s2)]
            if s1==s2:
                memo[(s1,s2)]=True
                return True
            if len(s1)!=len(s2):
                memo[(s1,s2)]=True
                return False
            if sorted(s1)!=sorted(s2):
                memo[(s1,s2)]=False
                return False
            n=len(s1)
            for i in range(1,n):
                case1=helper(s1[i:],s2[i:]) and helper(s1[:i],s2[:i])
                case2=helper(s1[i:],s2[:-i]) and helper(s1[:i],s2[-i:])
                if case1 or case2:
                    memo[(s1,s2)]=True
                    return True
            memo[(s1,s2)]=False
            return False
        return helper(s1,s2)