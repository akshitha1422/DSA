class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo={}
        MOD=10**9+7
        def helper(n,target):
            if n==0:
                return 1 if target==0 else 0
            if (n,target) in memo:
                return memo[(n,target)]
            ways=0
            for face in range(1,k+1):
                if target-face>=0:
                    ways+=helper(n-1,target-face)
                    ways%=MOD
            memo[(n,target)]=ways
            return ways
        return helper(n,target)