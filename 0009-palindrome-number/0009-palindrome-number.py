class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s1=str(x)
        # s2=str(x)[::-1]
        # if s1==s2:
        #     return True
        # else:
        #     return False
        sx=str(x)
        i=0
        j=len(sx)-1
        while i<j:
            if sx[i]!=sx[j]:
                return False
            i+=1
            j-=1
        return True