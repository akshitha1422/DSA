#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        n=len(arr)
        arr.sort()
        dep.sort()
        curr=0
        maxp=0
        i=0
        j=0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                curr+=1
                i+=1
            else:
                curr-=1
                j+=1
            maxp=max(maxp,curr)
        return maxp