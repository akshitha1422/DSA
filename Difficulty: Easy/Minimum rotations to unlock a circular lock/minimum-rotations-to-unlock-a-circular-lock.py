#User function Template for python3

class Solution:
    def rotationCount(self, R, D):
        rot=0
        while R and D:
            r=R%10
            d=D%10
            rot+=min(abs(r-d),10-abs(r-d))
            R=R//10
            D=D//10
        return rot