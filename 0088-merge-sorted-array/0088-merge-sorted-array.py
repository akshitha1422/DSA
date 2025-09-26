class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:]=nums1[:m]
        # nums1+=nums2
        # nums1.sort()
        res=[]
        p1=0
        p2=0
        while p1<m and p2<n:
            if nums1[p1]<=nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1
        for k in range(p1,m):
            res.append(nums1[k])
        for k in range(p2,n):
            res.append(nums2[k])
        for i in range(len(res)):
            nums1[i]=res[i]