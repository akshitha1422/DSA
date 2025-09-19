class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st={}
        for i,n in enumerate(nums):
            if (target-n) in st.keys():
                return [st[target-n],i]
            else:
                st[n]=i