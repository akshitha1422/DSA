class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for n in nums1:
            if n in nums2:
                nums2.remove(n)
                res.append(n)
        return res