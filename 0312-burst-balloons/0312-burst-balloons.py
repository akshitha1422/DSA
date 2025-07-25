class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        memo=[[0]*n for _ in range(n)]
        for i in range(2,n):
            for left in range(0,n-i):
                right=left+i
                for k in range(left+1,right):
                    memo[left][right]=max(memo[left][right],nums[left]*nums[k]*nums[right]+memo[left][k]+memo[k][right])
        return memo[0][n-1]
