class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq=Counter(nums)
        st=[]
        for i in freq.keys():
            if freq[i]>1:
                st.append(i)
        return st