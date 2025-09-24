class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st={}
        for i,n in enumerate(nums):
            if (target-n) in st:
                return [i,st[target-n]]
            else:
                st[n]=i