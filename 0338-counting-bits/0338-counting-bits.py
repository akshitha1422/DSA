class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans=[]
        # ans.append(0)
        # for i in range(1,n+1):
        #     a=bin(i)
        #     b=a.count('1')
        #     ans.append(int(b))
        # return ans



        ans=[0]*(n+1)
        for i in range(1,n+1):
            ans[i]=ans[i >> 1] + (i & 1)
        return ans