class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        res=[-1]*n
        starts=sorted((s,i) for i,(s,e) in enumerate(intervals))
        for i,(s,e) in enumerate(intervals):
            lo,hi=0,n-1
            idx=-1
            while lo<=hi:
                mid=(lo+hi)//2
                if starts[mid][0]>=e:
                    idx=starts[mid][1]
                    hi=mid-1
                else:
                    lo=mid+1
            res[i]=idx
        return res