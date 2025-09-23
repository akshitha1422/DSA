class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        new=0
        for i in nums:
            if i==1:
                new+=1
                count=max(new,count)
            else:
                new=0
        return count