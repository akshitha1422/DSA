class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            a=bin(i)
            res.append(str(a).count('1'))
        return res