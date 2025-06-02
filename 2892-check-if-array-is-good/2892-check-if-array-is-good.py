class Solution:
    def isGood(self, nums: List[int]) -> bool:
        l=float('-inf')
        for i in nums:
            if i>l:
                l=i
        if len(nums)==l+1:
            for i in range(1,len(nums)):
                if i not in nums:
                    return False
            if nums.count(l)!=2:
                return False
            else:
                return True
        else:
            return False