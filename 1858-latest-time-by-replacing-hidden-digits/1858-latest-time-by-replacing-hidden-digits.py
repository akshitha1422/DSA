class Solution:
    def maximumTime(self, time: str) -> str:
        hrs=list(time[:2])
        mins=list(time[3:])
        if hrs[0]=='?':
            if hrs[1]=='?' or hrs[1]<='3':
                hrs[0]='2'
            else:
                hrs[0]='1'
        if hrs[1]=='?':
            if hrs[0]=='2':
                hrs[1]='3'
            else:
                hrs[1]='9'
        if mins[0]=='?':
            mins[0]='5'
        if mins[1]=='?':
            mins[1]='9'
        return ''.join(hrs)+':'+''.join(mins)