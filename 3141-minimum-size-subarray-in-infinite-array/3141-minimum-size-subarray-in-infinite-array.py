class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        n=len(nums)
        full_repeats=target//total
        target=target%total
        if target==0:
            return full_repeats*n
        arr=nums+nums
        prefix=0
        l=0
        min_val=float('inf')
        for r in range(len(arr)):
            prefix+=arr[r]
            while prefix>target:
                prefix-=arr[l]
                l+=1
            if prefix==target:
                min_val=min(min_val,r-l+1)
        if min_val==float('inf'):
            return -1
        else:
            return min_val+full_repeats*n