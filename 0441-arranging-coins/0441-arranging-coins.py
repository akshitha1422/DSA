class Solution:
    def arrangeCoins(self, n: int) -> int:
        # rows=0
        # i=1
        # while n>0:
        #     if n>=i:
        #         rows+=1
        #         n-=i
        #     else:
        #         n-=i
        #     i+=1
        # return rows
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            curr=mid*(mid+1)//2
            if curr==n:
                return mid
            elif curr<n:
                left=mid+1
            else:
                right=mid-1
        return right