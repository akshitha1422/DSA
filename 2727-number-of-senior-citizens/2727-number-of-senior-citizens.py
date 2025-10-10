class Solution:
    def countSeniors(self, details: List[str]) -> int:
        i=11
        count=0
        for d in details:
            if int(d[i:i+2])>60:
                count+=1
        return count