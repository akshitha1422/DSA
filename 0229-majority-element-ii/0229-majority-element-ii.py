class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n=len(nums)
        freq=Counter(nums)
        st=[]
        for k,v in freq.items():
            if v>n/3:
                st.append(k)
        return st