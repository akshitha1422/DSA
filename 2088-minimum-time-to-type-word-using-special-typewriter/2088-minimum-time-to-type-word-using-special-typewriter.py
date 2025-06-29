class Solution:
    def minTimeToType(self, word: str) -> int:
        curr='a'
        count=0
        for i in word:
            if i==curr:
                count+=1
            else:
                cw=abs(ord(i)-ord(curr))
                ccw=26-cw
                count+=min(cw,ccw)+1
                curr=i
        return count