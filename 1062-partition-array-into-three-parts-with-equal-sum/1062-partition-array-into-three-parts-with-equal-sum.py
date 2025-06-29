class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3!=0:
            return False
        total=sum(arr)//3
        curr=0
        parts=0
        for i in range(len(arr)):
            curr+=arr[i]
            if curr==total:
                parts+=1
                curr=0
            if parts==2 and i<len(arr)-1:
                return True
        return False