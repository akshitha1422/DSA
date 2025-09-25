class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # nums=list(set(nums))
        # nums.sort()
        # count=1
        # curr=1
        # for i in range(len(nums)-1):
        #     if nums[i]+1==nums[i+1]:
        #         curr+=1
        #         count=max(count,curr)
        #     else:
        #         curr=1
        # return count
        nums=set(nums)
        count=0
        for n in nums:
            if n-1 not in nums:
                curr=1
                while n+curr in nums:
                    curr+=1
                count=max(count,curr)
        return count