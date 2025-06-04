class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # exp=0
        # s=0
        # for i in reversed(digits):
        #     s+=i*(10**exp)
        #     exp+=1
        # s=s+1
        # new=[]
        # while s>0:
        #     a=s%10
        #     new.insert(0,a)
        #     s=s//10
        # return new
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits