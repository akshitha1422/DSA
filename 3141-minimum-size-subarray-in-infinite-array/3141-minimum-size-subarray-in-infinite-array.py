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
        seen={0:-1}
        min_val=float('inf')
        for i,num in enumerate(arr):
            prefix+=num
            if prefix-target in seen:
                min_val=min(min_val,i-seen[prefix-target])
            if prefix not in seen:
                seen[prefix]=i
        if min_val==float('inf'):
            return -1
        else:
            return min_val+full_repeats*n