class Solution:
    def secondHighest(self, s: str) -> int:
        f=float('-inf')
        se=float('-inf')
        for i in range(len(s)):
            a=s[-1]
            s=s[:-1]
            if a.isdigit():
                a=int(a)
                if a>f and a!=f:
                    se=f
                    f=a
                elif a>se and a<f:
                    se=a
        if se==float('-inf'):
            se=-1
        return se