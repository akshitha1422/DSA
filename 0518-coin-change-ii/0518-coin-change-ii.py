class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo={}
        def helper(n,amount):
            if amount==0:
                return 1
            if n==0:
                return 0
            if (n,amount) in memo:
                return memo[(n,amount)]
            if coins[n-1]<=amount:
                memo[(n,amount)]=helper(n,amount-coins[n-1])+helper(n-1,amount)
            else:
                memo[(n,amount)]=helper(n-1,amount)
            return memo[(n,amount)]
        return helper(n,amount)