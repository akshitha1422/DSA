class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        st=str(num)
        count=0
        for i in range(len(st)-k+1):
            window=st[i:i+k]
            va=int(window)
            if va!=0 and num%va==0:
                count+=1
        return count