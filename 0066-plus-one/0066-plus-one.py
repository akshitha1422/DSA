class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        s1=''
        for d in digits:
            s1+=str(d)
        n=int(s1)+1
        s2=str(n)
        for i in s2:
            res.append(int(i))
        return res