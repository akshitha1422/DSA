class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
        for i in range(1,n+1):
            a=bin(i)
            b=a.count('1')
            ans.append(int(b))
        return ans