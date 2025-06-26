class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        have={5:0,10:0,20:0}
        for i in bills:
            if i==5:
                have[5]+=1
            elif i==10:
                if have[5]>0:
                    have[10]+=1
                    have[5]-=1
                else:
                    return False
            elif i==20:
                if have[10]>0 and have[5]>0:
                    have[20]+=1
                    have[10]-=1
                    have[5]-=1
                elif have[10]==0 and have[5]>=3:
                    have[20]+=1
                    have[5]-=3
                else:
                    return False
        return True