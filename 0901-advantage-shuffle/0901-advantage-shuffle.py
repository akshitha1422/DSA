class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sortnum2=sorted([(val,i) for i,val in enumerate(nums2)], key=lambda x:x[0])
        n=len(nums1)
        st=[0]*n
        low=0
        high=n-1
        i=n-1
        while i>=0:
            if nums1[high]>sortnum2[i][0]:
                st[sortnum2[i][1]]=nums1[high]
                high-=1
            else:
                st[sortnum2[i][1]]=nums1[low]
                low+=1
            i-=1
        return st