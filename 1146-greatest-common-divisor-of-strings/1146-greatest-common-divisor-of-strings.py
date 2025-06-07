class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)<len(str2):
            word=str1
        else:
            word=str2
        sub=''
        ans=''
        for i in word:
            sub=sub+i
            if str1==sub*(len(str1)//len(sub)) and str2==sub*(len(str2)//len(sub)):
                ans=sub
        return ans


        # if str1+str2!=str2+str1:
        #     return ''
        # else:
        #     gcd=math.gcd(len(str1),len(str2))
        # return str1[:gcd]