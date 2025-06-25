#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # meetings=[[start[i],end[i],i+1] for i in range(len(start))]
        # meetings.sort(key=lambda x:x[1])
        meetings = sorted(zip(end, start))
        num=0
        last=-1
        for e,s in meetings:
            if last<s:
                num+=1
                last=e
        return num