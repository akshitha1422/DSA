class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=float('inf')
        i=0
        while i<=len(nums)-k:
            diff=nums[i+k-1]-nums[i]
            count=min(count,diff)
            i+=1
        if count==float('inf'):
            return 0
        return count