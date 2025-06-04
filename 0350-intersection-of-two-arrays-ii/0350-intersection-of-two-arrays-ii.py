class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        for i in nums1:
            if i in nums2:
                st.append(i)
                nums2.remove(i)
        return st