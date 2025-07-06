class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        memo={}
        def helper(amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            min_val=float('inf')
            for c in coins:
                res=helper(amount-c)
                if res!=float('inf'):
                    min_val=min(min_val,res+1)
            memo[amount]=min_val
            return min_val
        result=helper(amount)
        return result if result!=float('inf') else -1