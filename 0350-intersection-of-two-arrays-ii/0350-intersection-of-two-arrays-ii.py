class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        ct=Counter(nums1)
        for i in nums2:
            if ct[i]>0:
                res.append(i)
                ct[i]-=1
        return res