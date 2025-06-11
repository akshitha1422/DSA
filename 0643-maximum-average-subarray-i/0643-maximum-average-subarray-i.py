class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        max_avg=window
        for i in range(k,len(nums)):
            window+=nums[i]-nums[i-k]
            max_avg=max(max_avg,window)
        return max_avg/k