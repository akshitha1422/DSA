class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        st=[[],[]]
        set1=set(nums1)
        set2=set(nums2)
        for i in set1:
            if i not in set2:
                st[0].append(i)
        for i in set2:
            if i not in set1:
                st[1].append(i)  
        return st