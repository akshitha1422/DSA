class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        if n==0:
            return 1.0
        if n<0:
            return 1/self.myPow(x,-n)
        half=self.myPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x