class Solution:
    def clumsy(self, n: int) -> int:
        if n==0 or n==1:
            return n
        elif n==2:
            return 2
        elif n==3:
            return 6
        elif n==4:
            return 7

        num=n * (n - 1) // (n - 2) + (n - 3)
        n-=4

        while n>=4:
            num -= (n * (n - 1)) // (n - 2) - (n - 3)
            n-=4
        if n==3:
            num-=3*2//1
        elif n==2:
            num-=2*1
        elif n==1:
            num-=1
        return num