class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st={}
        for i,num in enumerate(nums):
            if target-num in st:
                return [i,st[target-num]]
            else:
                st[num]=i