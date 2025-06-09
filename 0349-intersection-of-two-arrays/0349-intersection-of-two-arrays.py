class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        for i in nums1:
            if i in nums2:
                if i not in st:
                    st.append(i)
        return st